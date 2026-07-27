# Leucine AI Backend Assignment – FastAPI + RAG

A FastAPI-based backend application implementing a basic **Retrieval-Augmented Generation (RAG)** pipeline with JWT authentication, document ingestion, embeddings generation, similarity-based retrieval, and AI-powered question answering.

The application allows users to:

- Create an account and authenticate using JWT
- Upload text documents
- Process documents into smaller chunks
- Generate embeddings using Sentence Transformers
- Store document chunks and embeddings
- Retrieve relevant context using similarity search
- Ask questions and receive AI-generated answers

---

# 🚀 Features

## 🔐 Authentication

Implemented secure user authentication.

Features:

- User signup
- User login
- JWT-based authentication
- Password hashing using bcrypt
- Protected API access using Bearer tokens


## 📄 Document Management

Users can:

- Upload text documents
- Store document metadata
- Split documents into smaller chunks
- Generate embeddings for chunks
- Store chunks for retrieval


## 🧠 Retrieval-Augmented Generation (RAG)

The RAG pipeline includes:

- Text chunking
- Embedding generation
- Similarity-based retrieval
- Context-based answer generation


## ⚠️ Exception Handling

Custom FastAPI middleware is implemented for handling unexpected errors.

The middleware:

- Captures unhandled exceptions
- Logs errors into the database
- Returns standardized JSON error responses


---

# 🏗️ Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn


## Authentication

- JWT
- Python-JOSE
- Passlib
- bcrypt


## Database

- PostgreSQL
- SQLAlchemy ORM


## AI / RAG

- Sentence Transformers
- Hugging Face Models
- Embeddings
- Similarity Search
- OpenAI API integration


---

# 📂 Project Structure

```
Leucine-RAG-Assignment/

│
├── app/
│
│   ├── main.py
│
│   ├── api/
│   │   ├── auth.py
│   │   ├── documents.py
│   │   └── chat.py
│
│   ├── core/
│   │   ├── database.py
│   │   ├── security.py
│   │   └── config.py
│
│   ├── models/
│   │   ├── user.py
│   │   ├── document.py
│   │   ├── chunk.py
│   │   └── error_log.py
│
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── document_schema.py
│   │   └── chat_schema.py
│
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── document_service.py
│   │   ├── embedding_service.py
│   │   └── rag_service.py
│
│   └── middleware/
│       └── exception_logger.py
│
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── .markdownlint.json
```

---

# ⚙️ Installation and Setup

## 1. Clone Repository

```bash
git clone <repository-url>

cd Leucine-RAG-Assignment
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / Mac

```bash
python -m venv .venv

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

## Variable Description

| Variable | Description |
|----------|-------------|
| DATABASE_URL | PostgreSQL database connection URL |
| SECRET_KEY | Secret key used for JWT generation |
| ALGORITHM | JWT encryption algorithm |
| ACCESS_TOKEN_EXPIRE_MINUTES | JWT token expiry duration |
| HF_TOKEN | Hugging Face API token |

---

# ▶️ Running the Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Application runs at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🔐 Authentication Flow

1. User registers using `/auth/signup`.
2. Password is securely hashed using bcrypt.
3. User logs in using `/auth/login`.
4. Credentials are verified.
5. JWT access token is generated.
6. Token is used to access protected APIs.

For protected APIs:

```
Authorization: Bearer <access_token>
```

---

# 📄 Document Ingestion Flow

When a document is uploaded:

1. Document content is received through API.
2. Document metadata is stored.
3. Text is divided into smaller chunks.
4. Sentence Transformer generates embeddings.
5. Chunk data and embeddings are stored.
6. Stored embeddings are used during retrieval.


---

# 🔄 RAG Pipeline Flow


```
User uploads document

        |
        ↓

Document stored in database

        |
        ↓

Text extracted and divided into chunks

        |
        ↓

Chunks converted into embeddings

        |
        ↓

Embeddings stored

        |
        ↓

User asks question

        |
        ↓

Question converted into embedding

        |
        ↓

Similarity search retrieves relevant chunks

        |
        ↓

Relevant context sent to LLM

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

## Documents

### Upload Document

```
POST /documents/
```

Request:

```json
{
"title":"FastAPI Notes",
"content":"FastAPI is a modern Python framework."
}
```

---

## Chat

### Ask Question

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
"answer":"FastAPI is a modern Python framework."
}
```

---

# 🗄️ Database Design

## User Table

Stores:

- User ID
- Email
- Hashed Password


## Document Table

Stores:

- Document ID
- Title
- Content
- User reference


## Chunk Table

Stores:

- Chunk ID
- Document reference
- Text chunk
- Embedding information


## Error Log Table

Stores:

- Timestamp
- Endpoint
- HTTP Method
- Error Message
- Stack Trace
- User ID


---

# 🗂️ Database Indexing Strategy

Indexes are created to improve query performance.

## User Table

- Email field is indexed because login searches users using email.
- Unique constraint prevents duplicate accounts.


## Document Table

- User ID is indexed for faster retrieval of user documents.


## Chunk Table

- Document ID is indexed to quickly retrieve chunks belonging to a document.
- Embeddings are stored for similarity search.


## Error Log Table

- Timestamp is indexed to quickly access recent errors.
- Endpoint indexing helps debugging.


---

# ⚠️ Exception Handling Middleware

Custom middleware handles unexpected application errors.

It performs:

- Global exception capturing
- Error logging into PostgreSQL
- JSON error response generation


Logged information:

- Timestamp
- Endpoint
- HTTP method
- Error message
- Stack trace
- Authenticated user ID (if available)


Example response:

```json
{
    "error":"Internal Server Error",
    "message":"Something went wrong"
}
```

---

# 🧠 RAG Components Explanation

## Document Chunking

Large documents are divided into smaller pieces.

Benefits:

- Better retrieval accuracy
- Faster processing


## Embeddings

Text chunks are converted into numerical vectors using Sentence Transformer models.

These vectors represent semantic meaning.


## Similarity Search

User questions are converted into embeddings and compared with stored embeddings to find relevant information.


## Response Generation

Retrieved context is provided to the AI model to generate the final answer.

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

- FastAPI
- Uvicorn
- SQLAlchemy
- Alembic
- Pydantic
- Python-JOSE
- Passlib
- bcrypt
- Sentence Transformers
- Transformers
- Torch
- OpenAI
- Scikit-learn


---

# 🔒 Security

Implemented security features:

- Password hashing
- JWT authentication
- Environment variable configuration
- Protected secrets
- Secure API access


---

# 🚀 Future Improvements

Possible enhancements:

- Redis caching
- Kafka/message broker integration
- Background document processing
- Docker deployment
- Vector database integration (FAISS, ChromaDB)
- Streaming LLM responses
- Unit and integration testing


---

# 👩‍💻 Author

**Disha M D**

Information Science and Engineering


---

# 📄 License

This project is created as part of the Leucine AI Backend Assignment.
<!-- Updated repository metadata -->