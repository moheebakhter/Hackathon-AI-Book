from qdrant_client import QdrantClient, models
from src.core.config import settings

class QdrantDB:
    def __init__(self):
        self.client = QdrantClient(
            url=settings.QDRANT_URL, 
            api_key=settings.QDRANT_API_KEY
        )
        self.collection_name = settings.QDRANT_COLLECTION_NAME

    def search(self, vector: list[float], limit: int = 5) -> list[models.ScoredPoint]:
        """Performs a vector search in the Qdrant collection."""
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=limit,
            with_payload=True
        )
        return search_result

qdrant_db = QdrantDB()
