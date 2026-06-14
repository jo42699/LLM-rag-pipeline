# ingest.py
import os
import chromadb
from pypdf import PdfReader
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

load_dotenv()

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="text-embedding-3-small"
)

chroma_client = chromadb.PersistentClient(path="chroma_persistent_storage")

# reset collection
try:
    chroma_client.delete_collection("document_qa_collection")
except:
    pass

collection = chroma_client.get_or_create_collection(
    name="document_qa_collection",
    embedding_function=openai_ef
)

def load_pdf_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

chunk_size = 1500
overlap = 200

all_chunks = []
all_ids = []

for file in os.listdir("./pdf"):
    if file.endswith(".pdf"):
        text = load_pdf_text(os.path.join("./pdf", file))

        start = 0
        i = 0

        while start < len(text):
            chunk = text[start:start + chunk_size]

            all_chunks.append(chunk)
            all_ids.append(f"{file}_chunk_{i}")

            start += chunk_size - overlap
            i += 1

# batch insert
batch_size = 50

for i in range(0, len(all_chunks), batch_size):
    collection.add(
        documents=all_chunks[i:i+batch_size],
        ids=all_ids[i:i+batch_size]
    )

print("INGESTION COMPLETE")