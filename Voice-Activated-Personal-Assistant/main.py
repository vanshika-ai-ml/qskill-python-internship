import asyncio
import edge_tts
from playsound import playsound
import speech_recognition as sr
import os
import time
from datetime import datetime
import webbrowser
import requests
import winsound

API_KEY = "YOUR_WEATHER_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"


async def speak(text):
    communicate = edge_tts.Communicate(
        text,
        voice="en-IN-NeerjaNeural"
    )

    await communicate.save("voice.mp3")
    playsound("voice.mp3")
    time.sleep(0.5)

    if os.path.exists("voice.mp3"):
        os.remove("voice.mp3")

def listen():
    recogniser = sr.Recognizer()

    with sr.Microphone() as source:
        recogniser.adjust_for_ambient_noise(source, duration=0.3)
        recogniser.pause_threshold = 1
        recogniser.energy_threshold = 300
        recogniser.dynamic_energy_threshold = True
        print("🎤 Listening...  Please Speak now.")

        audio = recogniser.listen(source,timeout=5,phrase_time_limit=5)

    try:
        text = recogniser.recognize_google(audio)
        print("You said:", text)

        return text.lower()

    except Exception as e:
        print(e)
        return ""
    
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    return data

def get_news():

    url = f"https://newsapi.org/v2/everything?q=India&language=en&pageSize=3&sortBy=publishedAt&apiKey={NEWS_API_KEY}"

    response = requests.get(url)

    data = response.json()

    return data

def set_reminder(message, seconds):
    print(f"Reminder set for {seconds} seconds.")

    time.sleep(seconds)
    winsound.Beep(1000,500)

    print("🔔 Reminder:", message)
    asyncio.run(speak(f"Reminder. {message}"))

user_name = input("Enter your name:")
asyncio.run(speak(f"Hello {user_name}! I am Era, your personal AI assistant."))

while True:
    text = listen()

    if "hello" in text:
        response = f"Hello {user_name}! How are you?"
        print("Era:", response)
        asyncio.run(speak(response))

    elif "your name" in text:
        response = "My name is Era. I am your personal AI assistant."
        print("Era:", response)
        asyncio.run(speak(response))

    elif "time" in text:
        current_time = datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}"
        print("Era:", response)
        asyncio.run(speak(response))

    elif "date" in text:
        current_date = datetime.now().strftime("%d %B %Y")
        response = f"Today's date is {current_date}"
        print("Era:", response)
        asyncio.run(speak(response))

    elif "open google" in text:
        response = "Opening Google"
        print("Era:", response)
        asyncio.run(speak(response))
        webbrowser.open("https://www.google.com")

    elif "open youtube" in text:
        response = "Opening YouTube"
        print("Era:", response)
        asyncio.run(speak(response))
        webbrowser.open("https://www.youtube.com")

    elif "open github" in text:
        response = "Opening GitHub"
        print("Era:", response)
        asyncio.run(speak(response))
        webbrowser.open("https://github.com")
    
    elif "open chat gpt" in text or "open chat" in text or "open chatgpt" in text:
        response = "Opening ChatGPT"
        print("Era:", response)
        asyncio.run(speak(response))
        webbrowser.open("https://chatgpt.com")

    elif "open calculator" in text:
        response = "Opening Calculator"
        print("Era:", response)
        asyncio.run(speak(response))
        os.system("calc")

    elif "weather" in text:
        response = "Please tell me the city name."
        print("Era:", response)
        asyncio.run(speak(response))
        city = listen()
        weather = get_weather(city)
        if weather["cod"] == 200:
            temperature = round(weather["main"]["temp"],1)
            description = weather["weather"][0]["description"]
            response = f"The temperature in {city.title()} is {temperature} degrees Celsius with {description}."
        else:
            response = "Sorry, I couldn't find that city."
            
        print("Era:", response)
        asyncio.run(speak(response))


    elif "news" in text:
        response = "Here are today's top headlines."
        print("Era:", response)
        asyncio.run(speak(response))
        news = get_news()
        
        if news["status"] == "ok" and len(news["articles"]) > 0 :
            articles = news["articles"]
            for article in articles[:3]:
                headline = article["title"].split(" - ")[0]
                print("Era:", headline)
                asyncio.run(speak(headline))
        else:
            response = "Sorry, I couldn't fetch the news."
           
            print("Era:", response)
            asyncio.run(speak(response))
    
    elif "reminder" in text:

        response = "What should I remind you?"
        print("Era:", response)
        asyncio.run(speak(response))

        message = listen()

        response = "After how many seconds?"
        print("Era:", response)
        asyncio.run(speak(response))

        seconds = int(input("Enter reminder time in seconds: "))

        response = f"Okay. I will remind you in {seconds} seconds."
        print("Era:", response)
        asyncio.run(speak(response))

        set_reminder(message, seconds)
        

    elif "exit" in text or "goodbye" in text or "bye" in text:
        response = f"Goodbye {user_name}! Have a nice day."
        print("Era:", response)
        asyncio.run(speak(response))
        break

    elif text == "":
        response = "I couldn't hear you. Please try again"
        print("Era:", response)
        asyncio.run(speak(response))

    else:
        response = "Sorry, I don't know that command yet."
        print("Era:", response)
        asyncio.run(speak(response))



