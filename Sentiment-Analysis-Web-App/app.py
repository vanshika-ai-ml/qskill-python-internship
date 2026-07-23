from flask import Flask, render_template, request
from textblob import TextBlob
app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def home():

    if request.method == "POST":

        text = request.form["text"]

        blob = TextBlob(text)

        polarity = blob.sentiment.polarity

        if polarity > 0:
            result = "😊 Positive"

        elif polarity < 0:
            result = "😞 Negative"

        else:
            result = "😐 Neutral"

        return render_template("index.html",result=result,text=text,polarity = round(polarity,2))

    return render_template("index.html",result = None, text="",polarity = None)

if __name__ == "__main__":
    app.run(debug=True)
