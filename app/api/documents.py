from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import traceback

from app.core.database import get_db
from app.schemas.document_schema import DocumentCreate, DocumentResponse
from app.services.document_service import create_document
from app.core.security import get_current_user


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/", response_model=DocumentResponse)
def upload_document(
    document: DocumentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    try:
        new_document = create_document(
            db,
            document.title,
            document.content
        )

        return new_document

    except Exception as e:
        print("========== DOCUMENT ERROR ==========")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))