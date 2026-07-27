from fastapi import FastAPI

from app.core.database import Base, engine

from app.models import *

from app.api.auth import router as auth_router
from app.api.documents import router as document_router
from app.api.chat import router as chat_router


print(Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Leucine AI Backend Assignment"
)


app.include_router(auth_router)
app.include_router(document_router)
app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "FastAPI Backend is Running 🚀"
    }