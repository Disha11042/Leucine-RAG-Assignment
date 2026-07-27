from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.chunk import Chunk

from app.services.rag_service import chunk_text
from app.services.embedding_service import generate_embedding


def create_document(
    db: Session,
    title: str,
    content: str
):

    # Save document
    document = Document(
        title=title,
        content=content
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    # Split document into chunks
    chunks = chunk_text(content)

    # Generate embedding and save each chunk
    for chunk in chunks:

        embedding = generate_embedding(chunk)

        new_chunk = Chunk(
            document_id=document.id,
            chunk_text=chunk,
            embedding=str(embedding)
        )

        db.add(new_chunk)

    db.commit()

    return document