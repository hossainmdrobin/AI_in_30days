from groq import Groq

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

messages = []

while True:
    user_input = input("You: ")
    messages.append({"role":"user","content":user_input})

    if user_input.lower() == "exit":
        break
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({'role':'assistant',"content":reply})

    print("AI: ", reply)