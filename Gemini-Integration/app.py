from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    prompt = ""

    if request.method == "POST":
        prompt = request.form["prompt"]
        
        result = client.models.generate_content(model = "gemini-flash-latest", contents = f"Answer in 5-6 lines only: {prompt} ")
        response = result.text

    return render_template("index.html", response=response , prompt = prompt)

if __name__ == "__main__":
    app.run(debug=True)
