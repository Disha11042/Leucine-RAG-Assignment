from app.services.embedding_service import generate_embedding
import math


def chunk_text(
    text: str,
    chunk_size: int = 200
):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def cosine_similarity(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))

    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))

    if norm1 == 0 or norm2 == 0:
        return 0

    return dot / (norm1 * norm2)


def retrieve_best_chunk(question, chunks):

    question_embedding = generate_embedding(question)

    best_score = -1
    best_chunk = ""

    for chunk in chunks:

        embedding = eval(chunk.embedding)

        score = cosine_similarity(
            question_embedding,
            embedding
        )

        if score > best_score:
            best_score = score
            best_chunk = chunk.chunk_text

    return best_chunk