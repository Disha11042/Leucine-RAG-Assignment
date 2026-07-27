# Leucine AI Backend Assignment

A FastAPI-based backend application that implements a **Retrieval Augmented Generation (RAG)** pipeline for document upload and intelligent question answering.

The application allows users to:
- Create an account and authenticate using JWT
- Upload documents
- Process documents into searchable chunks
- Generate embeddings using Sentence Transformers
- Retrieve relevant document context
- Ask questions and receive AI-generated answers based on uploaded documents

---

# 🚀 Features

## Authentication
- User signup
- User login
- JWT-based authentication
- Password hashing using bcrypt

## Document Management
- Upload text documents
- Store document metadata
- Split documents into smaller chunks
- Generate embeddings for document chunks

## RAG-based Chat System
- Accept user questions
- Convert queries into embeddings
- Retrieve relevant document chunks
- Generate contextual answers
- Return AI-powered responses

## Database
- SQLAlchemy ORM integration
- Database models for:
  - Users
  - Documents
  - Document Chunks
  - Error Logs

---

# 🏗️ Tech Stack

## Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic

## Authentication
- JWT Authentication
- Passlib
- bcrypt

## Database
- PostgreSQL
- SQLAlchemy ORM

## AI / RAG
- Sentence Transformers
- Hugging Face Models
- Vector Embeddings
- Similarity Search

## Server
- Uvicorn

---

# 📂 Project Structure

```
Leucine-RAG-Assignment/

│
├── app/
│   │
│   ├── main.py
│   │
│   ├── api/
│   │   ├── auth.py
│   │   ├── documents.py
│   │   └── chat.py
│   │
│   ├── core/
│   │   ├── database.py
│   │   ├── security.py
│   │   └── config.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── document.py
│   │   ├── chunk.py
│   │   └── error_log.py
│   │
│   ├── schemas/
│   │   ├── auth_schema.py
│   │   ├── document_schema.py
│   │   └── chat_schema.py
│   │
│   └── services/
│       ├── document_service.py
│       └── rag_service.py
│
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
└── alembic/
```

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

```bash
git clone <repository-url>

cd Leucine-RAG-Assignment
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=your_database_url_here

SECRET_KEY=your_secret_key_here

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

HF_TOKEN=your_huggingface_token_here
```

---

# ▶️ Running the Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

Swagger API Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🔄 RAG Pipeline Flow

```
User uploads document
          |
          ↓
Document stored in database
          |
          ↓
Text extracted and split into chunks
          |
          ↓
Chunks converted into embeddings
          |
          ↓
Embeddings stored
          |
          ↓
User asks a question
          |
          ↓
Question converted into embedding
          |
          ↓
Similarity search finds relevant chunks
          |
          ↓
Relevant context provided to AI model
          |
          ↓
Generated answer returned
```

---

# 📌 API Endpoints

## Authentication

### Signup

```
POST /auth/signup
```

Request:

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

Response:

```json
{
  "id":1,
  "email":"user@example.com"
}
```

---

### Login

```
POST /auth/login
```

Request:

```json
{
  "email":"user@example.com",
  "password":"password123"
}
```

Response:

```json
{
  "access_token":"jwt_token",
  "token_type":"bearer"
}
```

---

# Documents

## Upload Document

```
POST /documents/
```

Request:

```json
{
"title":"FastAPI Notes",
"content":"FastAPI is a modern Python framework used to build APIs."
}
```

Response:

```json
{
"id":1,
"title":"FastAPI Notes"
}
```

---

# Chat

## Ask Question

```
POST /chat/
```

Request:

```json
{
"question":"What framework is used to build APIs?"
}
```

Response:

```json
{
"answer":"FastAPI is a modern Python framework used to build APIs."
}
```

---

# 🗄️ Database Models

## User

Stores:
- User ID
- Email
- Hashed Password


## Document

Stores:
- Document ID
- Title
- Content


## Chunk

Stores:
- Chunk ID
- Document reference
- Text chunk
- Embedding information


## Error Log

Stores:
- Error details
- Timestamp

---

# 🧠 RAG Components Explanation

## Document Chunking

Large documents are divided into smaller sections called chunks.

Benefits:
- Improves retrieval accuracy
- Reduces processing complexity


## Embeddings

Text chunks are converted into numerical vectors using Sentence Transformer models.

These vectors represent semantic meaning.


## Similarity Search

The user's question embedding is compared with document embeddings to find the most relevant information.


## Response Generation

The retrieved context is used to generate a meaningful answer related to the uploaded documents.

---

# 🧪 Testing

APIs can be tested using:

- Swagger UI
- Postman
- Curl

Swagger:

```
http://127.0.0.1:8000/docs
```

---

# 📦 Dependencies

Main packages:

```
FastAPI
Uvicorn
SQLAlchemy
Alembic
Pydantic
Python-JOSE
Passlib
bcrypt
Sentence Transformers
Transformers
Torch
OpenAI
Scikit-learn
```

---

# 🔒 Security

Implemented security features:

- Password hashing
- JWT authentication
- Environment variable based configuration
- Protected secrets

---

# 👩‍💻 Author

Disha M D

Information Science and Engineering

---

# 📄 License

This project is created as part of the Leucine AI Backend Assignment.