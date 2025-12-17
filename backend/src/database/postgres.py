import asyncpg
from src.core.config import settings
from src.schemas.chat import Source
from typing import List

class PostgresDB:
    def __init__(self):
        self.db_url = settings.DATABASE_URL
        self._pool = None

    async def get_pool(self):
        if self._pool is None:
            self._pool = await asyncpg.create_pool(self.db_url)
        return self._pool

    async def get_sources_by_ids(self, chunk_ids: List[str]) -> List[Source]:
        """
        Fetches source metadata for a list of chunk IDs.
        NOTE: This assumes a table named 'chunks' with columns
        'chunk_id', 'file_path', 'chapter_title', 'section_heading'.
        The actual schema needs to be created during the data preparation phase.
        """
        if not chunk_ids:
            return []

        pool = await self.get_pool()
        query = """
            SELECT file_path, chapter_title, section_heading
            FROM chunks
            WHERE chunk_id = ANY($1::text[])
        """
        async with pool.acquire() as connection:
            records = await connection.fetch(query, chunk_ids)
        
        return [Source(**record) for record in records]

postgres_db = PostgresDB()
