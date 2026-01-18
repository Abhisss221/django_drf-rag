
# 🧠 Django + RAG (Local, Open-Source)

This project shows how to build a **Django backend** that can answer questions using **RAG (Retrieval Augmented Generation)** with a **local LLM (Ollama)**.

⚠️ **Note:**
This project is written for **beginners**.
If you are already experienced with LangChain / RAG / Django internals, this repo may feel too basic.

---

## 🚀 What This Project Does (In Simple Words)

1. You store documents (text files)
2. They are converted into embeddings and saved in a vector database (FAISS)
3. A user asks a question via an API
4. The system:

   * Finds relevant document chunks
   * Sends them to a local LLM (LLaMA via Ollama)
5. The answer is returned as a JSON response

👉 No OpenAI
👉 No paid APIs
👉 Everything runs **locally**

---

## 🧩 Tech Stack

* **Backend:** Django + Django REST Framework
* **LLM:** Ollama (LLaMA models)
* **RAG:** LangChain
* **Vector DB:** FAISS
* **Embeddings:** Sentence Transformers (open-source)

---

## 📁 Project Structure

```
rag_project/
│
├── api/                    # Django REST APIs
│   ├── views.py
│   ├── serializers.py
│
├── rag/                    # RAG logic (framework independent)
│   ├── data/
│   │   └── docs.txt        # Knowledge source
│   ├── ingest.py           # Create FAISS index
│   ├── rag_chain.py        # Retriever + LLM
│   ├── rag_service.py      # Bridge between Django & RAG
│   ├── ask.py              # CLI testing
│   └── faiss_index/        # Saved vector database
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔁 How the System Works (Flow)

### 1️⃣ Ingestion (One Time)

```
docs.txt
   ↓
Text Splitter
   ↓
Embeddings
   ↓
FAISS Vector DB (saved locally)
```

Run:

```bash
python rag/ingest.py
```

---

### 2️⃣ Asking a Question (Runtime)

```
Client (POST /api/ask)
   ↓
Django API
   ↓
RAG Service
   ↓
FAISS Retriever
   ↓
Ollama (LLM)
   ↓
Answer (JSON)
```

---

## ▶️ How to Run the Project

### 1️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3️⃣ Make sure Ollama is running

```bash
ollama list
```

---

### 4️⃣ Create the vector database

```bash
python rag/ingest.py
```

You should see:

```
FAISS index created successfully
```

---

### 5️⃣ Start Django server

```bash
python manage.py runserver
```

---

### 6️⃣ Test the API

**Endpoint**

```
POST http://127.0.0.1:8000/api/ask/
```

**Body**

```json
{
  "question": "What is RAG?"
}
```

**Response**

```json
{
  "question": "What is RAG?",
  "answer": "RAG stands for Retrieval Augmented Generation..."
}
```

---

## 🧠 Important Design Decisions (Beginner Explanation)

* **RAG loads once**
  FAISS and the LLM are loaded only once to avoid slow responses.

* **AI logic is NOT inside Django views**
  Django only handles requests.
  RAG logic lives in a separate service (`rag_service.py`).

* **Local LLM**
  Ollama is used so no internet or API keys are required.

---

## ❌ What This Project Does NOT Do

* No authentication
* No document upload API
* No chat history
* No streaming responses
* No cloud deployment

These are intentionally skipped to keep things simple.

---

## 🧪 Who This Project Is For

✅ Django beginners
✅ People learning RAG from scratch
✅ Anyone who wants a **clean mental model**

❌ Advanced LangChain users
❌ Production-ready enterprise systems
❌ Multi-tenant AI platforms

---

## 📌 Next Possible Improvements (Optional)

* Upload PDFs and auto-reindex
* User-specific knowledge bases
* Chat history / memory
* Streaming responses
* Voice → RAG → Voice

---

## 🙌 Final Note

This project focuses on **understanding the flow**, not just making things “work”.

If you understand:

* why ingestion is separate
* why RAG is outside Django
* why the API layer is thin

👉 you are learning it the **right way**.

Happy building 🚀
