from flask import Flask, render_template, request
from groq import Groq

app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

@app.route("/",methods=["GET","POST"])
def home():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["message"]

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role":"user","content":user_input}]
        )

        response_text = response.choices[0].message.content
    return render_template("index.html", response=response_text)
if __name__ == "__main__":
    app.run(debug=True)
