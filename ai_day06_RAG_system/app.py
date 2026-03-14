from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss 
import numpy as np
from groq import Groq

reader = PdfReader("document.pdf")
text = ""
for page in reader.pages:
    text+=page.extract_text()
chunks = []
chunk_size = 500

for i in range(0,len(text),chunk_size):
    chunks.append(text[i:i+chunk_size])

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

query = input("Ask question: ")

query_embedding = model.encode([query])
D,I = index.search(np.array(query_embedding),k=3)

result = [chunks[i] for i in I[0]]

context = "\n".join(result)

print("Relevant text: ")

# print(context)
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role":"user","content":prompt}]
)

print(response.choices[0].message.content)





