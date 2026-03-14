from flask import Flask, render_template, request
from groq import Groq
import os

app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

@app.route("/", methods=["GET","POST"])
def home():

    result = ""

    if request.method == "POST":

        topic = request.form["topic"]
        platform = request.form["platform"]

        prompt = f"""
        Create social media content.

        Topic: {topic}
        Platform: {platform}

        Generate:
        1. Caption
        2. 10 hashtags
        3. Content idea
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role":"user","content":prompt}]
        )

        result = response.choices[0].message.content

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)