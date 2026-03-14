
topic = input("Enter YouTube video topic: ")

from groq import Groq

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

prompt = f"""
Create a YouTube video script for the topic:

{topic}

Include:
1. Video title
2. Attention-grabbing hook
3. Script outline
4. Key talking points
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role":"user","content":prompt}]
)

script = response.choices[0].message.content

print("\nGenerated Script:\n")
print(script)

import os

os.makedirs("scripts", exist_ok=True)

with open("scripts/script.txt","w") as f:
    f.write(script)

print("Script saved.")