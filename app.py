# app.py
import os
import chromadb
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from chromadb.utils import embedding_functions

load_dotenv()

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=openai_api_key,
    model_name="text-embedding-3-small"
)

chroma_client = chromadb.PersistentClient(path="chroma_persistent_storage")

collection = chroma_client.get_collection(
    name="document_qa_collection",
    embedding_function=openai_ef
)

@app.post("/chat")
def chat(req: QueryRequest):

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
                "content": f"Answer ONLY using this context:\n{context}"
            },
            {
                "role": "user",
                "content": req.query
            }
        ],
        temperature=0.2,
        max_tokens=1700
    )

    return {"response": response.choices[0].message.content}