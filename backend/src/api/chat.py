from fastapi import APIRouter, HTTPException
from src.models.rag import rag_model
from src.schemas.chat import QueryRequest, QueryResponse

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest):
    """
    Receives a user query, processes it through the RAG pipeline,
    and returns a grounded answer.
    """
    if not request.question:
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    
    try:
        response = await rag_model.query(request)
        return response
    except Exception as e:
        # In a real app, log the error properly
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred while processing the query.")
