import os
from dotenv import load_dotenv
from openai import OpenAI
import chromadb 
from chromadb.utils import embedding_functions
from pypdf import PdfReader
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    query: str   

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=openai_api_key,
    model_name="text-embedding-3-small"
)

chroma_client = chromadb.PersistentClient(path="chroma_persistent_storage")

collection = chroma_client.get_or_create_collection(
    name="document_qa_collection",
    embedding_function=openai_ef
)

client = OpenAI(api_key=openai_api_key)


# function to load documents
def load_documents_to_chromadb(directory_path):
    print("LOADING DOCUMENTS")
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory_path, filename)
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            documents.append({"id": filename, "text": text})
    return documents


# LOAD DOCS
directory_path = "./pdf"
documents = load_documents_to_chromadb(directory_path)

print("ADDING TO CHROMADB")

all_chunks = []
all_ids = []

chunk_size = 1000
overlap = 200

for doc in documents:
    text = doc["text"]
    start = 0
    i = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        all_chunks.append(chunk)
        all_ids.append(f"{doc['id']}_chunk_{i}")

        i += 1
        start += chunk_size - overlap


collection.add(
    documents=all_chunks,
    ids=all_ids
)

print("DONE")


# POST ROUTE for fastapi
@app.post("/chat")
def chat(req: QueryRequest):

    print("USER:", req.query)

    results = collection.query(
        query_texts=[req.query],
        n_results=3
    )

    context = "\n".join(results["documents"][0])

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": f"Answer using ONLY this context:\n{context}"
            },
            {
                "role": "user",
                "content": req.query
            }
        ],
        max_tokens=300,
        temperature=0.2
    )

    return {
        "response": response.choices[0].message.content
    }


