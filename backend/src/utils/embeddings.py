from openai import OpenAI
from src.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def get_embedding(text: str) -> list[float]:
    """Generates an embedding for a given text."""
    text = text.replace("\n", " ")
    response = client.embeddings.create(
        input=[text],
        model=settings.EMBEDDING_MODEL
    )
    return response.data[0].embedding
