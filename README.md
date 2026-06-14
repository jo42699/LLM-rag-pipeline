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




# Why I Made This

The preferred answer would be that I wanted to learn RAG and improve my skills, blah blah. Which is true, but the real motivation was that I was too lazy to read a book or, to put it more professionally, I didn't have enough time to read it.

The book was around 400 pages long, and I needed it for a paper I was writing. It was about some boring history topic that's not important right now. I tried using ChatGPT to help, but it was pretty useless because there was no way it was taking in all 400 pages of a PDF. I also looked online for general-purpose RAG systems, and they were charging up to $50 a month (CRIMINALS). Anyhow, there was no way I was paying that price. Not because I didn't have the money... okay, fine, I didn't have the money.

So I did what any reasonable person would do: I watched a few YouTube tutorials and learned how to build my own RAG system using Chroma and vector embeddings. I read a couple of research papers along the way, and one that I found especially insightful was *Vector Embeddings: The Mathematical Foundation of Modern AI Systems* by Vijay Vaibhav Singh.

After that, I built a chatbot using vanilla JavaScript and Node.js, connected it to a FastAPI backend, and BADABIM BADABOOM I had my own RAG system. I already had an OpenAI API key from September 2025, and after putting about $5 of credit on it, I've used less than $0.15 worth of tokens. I've been using the system for research for the last two months and have already ingested four books into it.

So yes, I learned about RAG, embeddings, vector databases, and API integration. But the entire project started because I didn't want to read a 400 page history book.






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







