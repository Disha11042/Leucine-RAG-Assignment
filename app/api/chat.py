from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.chunk import Chunk

from app.schemas.chat_schema import (
    ChatRequest,
    ChatResponse
)

from app.services.rag_service import retrieve_best_chunk

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "/",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    chunks = db.query(Chunk).all()

    answer = retrieve_best_chunk(
        request.question,
        chunks
    )

    return {
        "answer": answer
    }