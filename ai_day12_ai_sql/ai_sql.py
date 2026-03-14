from groq import Groq
import sqlite3

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

question = input("Ask about posts: ")

prompt = f"""
Convert the following question into SQL.

Table: posts
Columns: id, name, likes, comments

Question:
{question}

Return only SQL.
"""

response = client.chat.completions.create(
model="llama-3.1-8b-instant",
messages=[{"role":"user","content":prompt}]
)

sql_query = response.choices[0].message.content
sql_query = response.choices[0].message.content

# Remove markdown formatting
sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
# print("Generated SQL:")
# print(sql_query)
conn = sqlite3.connect("social.db")

cursor = conn.cursor()

cursor.execute(sql_query)

result = cursor.fetchall()

explain_prompt = f"""
Explain this database result clearly.

User question:
{question}

Database result:
{result}
"""
print("the Prompt: ", explain_prompt)

response = client.chat.completions.create(
model="llama-3.1-8b-instant",
messages=[{"role":"user","content":explain_prompt}]
)

print("AI Explanation:")
print(response.choices[0].message.content)