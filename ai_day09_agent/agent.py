import wikipedia
from groq import Groq

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=3)
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return "No result found"
    
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

question = input("Ask Question: ")

wiki_data = search_wikipedia(question)
print("The wikidata: ",{wiki_data})

prompt = f"""
You are a research assitant.
Information: 
{wiki_data}

Explain the topic clearly
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role":"user","content":prompt}]
)

print(response.choices[0].message.content)