product_name = input("Enter product name: ")
features = input("Enter product features: ")


from groq import Groq

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

prompt = f"""
Write a compelling product description.

Product Name: {product_name}
Features: {features}

Include:
- marketing tone
- key benefits
- short SEO-friendly description
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role":"user","content":prompt}]
)

description = response.choices[0].message.content

print("\nGenerated Description:\n")
print(description)
import os

os.makedirs("outputs", exist_ok=True)

with open("outputs/product_description.txt","w") as f:
    f.write(description)

print("Description saved.")
