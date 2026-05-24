# 📚 RAG Chatbot (FastAPI + Node + ChromaDB + OpenAI)

This project is a full-stack Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions about PDF documents using semantic search (ChromaDB) and OpenAI GPT models.

---

# 🚀 Tech Stack

## Backend (AI + RAG)
- Python
- FastAPI
- OpenAI API (GPT + Embeddings)
- ChromaDB (Vector Database)
- PyPDF (PDF text extraction)
- python-dotenv

## Middleware / Proxy Server
- Node.js
- Express.js
- Axios
- CORS
- Path module

## Frontend
- HTML
- CSS
- JavaScript (Vanilla) 

---

# 🧩 Architecture

Frontend (HTML/JS)
        ↓
Node.js Server (Port 3000)
        ↓
FastAPI Backend (Port 8000)
        ↓
ChromaDB Vector Search
        ↓
OpenAI API (GPT Response)

---



---

# ⚙️ Setup Instructions

## 1. Clone Project
git clone <repo-url>
cd RAG

---

## 2. Python Setup

python -m venv venv
venv\Scripts\activate   # Windows

pip install fastapi uvicorn openai chromadb python-dotenv pypdf

---

## 3. Node Setup

npm init -y
npm install express axios cors nodemon

(optional)
npm install -g nodemon

Run:
node server.js

---

## 4. Environment Variables

Create .env file:

OPENAI_API_KEY=your_api_key_here

---

## 5. Run FastAPI Backend

uvicorn app:app --reload

Runs on:
http://localhost:8000

---

## 6. Run Node Server

node server.js

Runs on:
http://localhost:3000

---

## 7. Open Frontend

http://localhost:3000

---

# 💬 How It Works

User → Frontend → Node (/chat) → FastAPI → ChromaDB → OpenAI → Response

---

# 📦 Features

- PDF ingestion (PyPDF)
- Text chunking
- Embeddings (OpenAI)
- Vector search (ChromaDB)
- RAG-based QA
- Node proxy layer
- Chat UI

---


## Empty body issue
Ensure:
app.use(express.json())

---

## CORS issues
Solved using Node proxy

---

## ChromaDB duplicate error
Do not reinsert same IDs on reload

---

# 🧠 Future Improvements

- Streaming responses (ChatGPT typing)
- Chat memory
- File upload UI
- Auth system
- Docker deployment
- Cloud hosting

---

# 👨‍💻 Author

RAG chatbot built for learning:
- LLM integration
- Vector databases
- Full-stack AI systems



```bash
pip install fastapi
pip install uvicorn
pip install openai
pip install chromadb
pip install python-dotenv
pip install pypdf


```npm 
npm install express
npm install axios
npm install cors
npm install path


