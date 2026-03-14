import os
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from groq import Groq

documents = []
folder = "docs"
for file in os.listdir(folder):
    if file.endswith(".pdf"):
        reader = PdfReader(os.path.join(folder,file))
        text = ""
        for page in reader.pages:
            text += page.extract_text()
            documents.append(text)
    
print("Loaded documents: ", len(documents))
chunks = []
chunk_size = 500

for doc in documents:
    for i in range(0, len(doc),chunk_size):
        chunks.append(doc[i:i+chunk_size])

print("Total chunks: ", len(chunks))

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

dimension = embeddings.shape[1]
# print(dimension)
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

query = input("Ask qustion: ")
query_embedding = model.encode([query])
D, I = index.search(np.array(query_embedding), k=3)
results = [chunks[i] for i in I[0]]

context = "\n".join(results)

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