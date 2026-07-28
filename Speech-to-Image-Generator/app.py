from flask import Flask , render_template
import speech_recognition as sr
from flask import request
import os
import requests
from urllib.parse import quote

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        'index.html',
        speech="🎤 Click the button and speak clearly.",
        image=None,
        error =None
    )


@app.route("/listen", methods=["POST"])
def listen():

    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 250
    recognizer.pause_threshold = 1.2
    recognizer.dynamic_energy_threshold = True

    with sr.Microphone() as source:

        print("Speak now...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source, timeout=5,phrase_time_limit=8)

    try:

        speech = recognizer.recognize_google(audio)
        display_text = "🗣️ " + speech

        print(speech)
        print("Generating Image...")

        prompt = quote(speech)

        image_url = f"https://image.pollinations.ai/prompt/{prompt}"

    except Exception as e:
        print(e)

        return render_template(
          "index.html",
          speech="🎤 " + speech if 'speech' in locals() else "",
          image=None,
          error="⚠️ Couldn't generate the image. Please try another prompt."
    )

    return render_template(
        "index.html",
        speech=display_text,
        image=image_url
    )


if __name__ == '__main__':
    app.run(debug=True)
