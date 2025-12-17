from openai import OpenAI
from typing import List

from src.core.config import settings
from src.database.qdrant import qdrant_db
from src.database.postgres import postgres_db
from src.schemas.chat import QueryRequest, QueryResponse, Source
from src.utils.embeddings import get_embedding
from src.utils.prompts import RAG_PROMPT_TEMPLATE

class RAGModel:
    def __init__(self):
        self.llm_client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.completion_model = settings.COMPLETION_MODEL

    async def _process_general_query(self, question: str) -> QueryResponse:
        """Handles a general query using the RAG pipeline."""
        query_vector = get_embedding(question)
        
        # Search Qdrant for relevant chunks
        search_results = qdrant_db.search(vector=query_vector, limit=5)
        
        if not search_results:
            return QueryResponse(answer="I'm sorry, I couldn't find any relevant information on that topic in the book.")

        # Extract context and chunk IDs
        context_text = "\n\n".join([point.payload['text'] for point in search_results])
        chunk_ids = [point.payload['chunk_id'] for point in search_results]

        # Fetch metadata from Postgres
        sources = await postgres_db.get_sources_by_ids(chunk_ids)

        # Generate response using LLM
        prompt = RAG_PROMPT_TEMPLATE.format(context=context_text, question=question)
        
        response = self.llm_client.chat.completions.create(
            model=self.completion_model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."}, 
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
        )
        
        answer = response.choices[0].message.content
        return QueryResponse(answer=answer.strip(), sources=sources)

    async def _process_selected_text_query(self, question: str, selected_text: str) -> QueryResponse:
        """Handles a query based only on user-selected text."""
        prompt = RAG_PROMPT_TEMPLATE.format(context=selected_text, question=question)
        
        response = self.llm_client.chat.completions.create(
            model=self.completion_model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."}, 
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
        )
        
        answer = response.choices[0].message.content
        return QueryResponse(answer=answer.strip(), sources=[])

    async def query(self, request: QueryRequest) -> QueryResponse:
        """Processes a query based on its type."""
        if request.selected_text:
            return await self._process_selected_text_query(request.question, request.selected_text)
        else:
            return await self._process_general_query(request.question)

rag_model = RAGModel()
