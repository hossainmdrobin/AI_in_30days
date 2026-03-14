import pandas as pd

df = pd.read_csv("insites_data.csv")
print("Dataset preview:")
# print(df.head())

# print("\nSummary statistics:")
# print(df.describe())
summary = df.describe().to_string()

print(summary)
from groq import Groq

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

prompt = f"""
You are a data analyst.

Analyze this dataset summary:

{summary}

Provide:
1. Key insights
2. Trends
3. Recommendations
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role":"user","content":prompt}]
)

print(response.choices[0].message.content)

top_post = df.loc[df['likes'].idxmax()]

print("Top performing post:")
print(top_post)