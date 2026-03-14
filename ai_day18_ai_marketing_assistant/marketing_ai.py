from groq import Groq
import os

print("AI Marketing Assistant")

print("1. Social Media Caption")
print("2. Marketing Email")
print("3. Product Description")
print("4. Blog Idea")

choice = input("Choose option: ")
topic = input("Enter topic: ")

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

prompt = f"""
You are a marketing expert.

Generate {choice} about this topic:

Topic: {topic}

Make it engaging and professional.
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role":"user","content":prompt}]
)

result = response.choices[0].message.content

print("\nGenerated Content:\n")
print(result)

os.makedirs("outputs", exist_ok=True)

with open("outputs/marketing_output.txt","w") as f:
    f.write(result)

print("Content saved.")
