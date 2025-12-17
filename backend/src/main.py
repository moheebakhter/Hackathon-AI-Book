from fastapi import FastAPI
from src.api.chat import router as chat_router

app = FastAPI(
    title="RAG Chatbot Backend",
    description="Backend service for the Integrated RAG Chatbot.",
    version="0.1.0",
)

# Include the chat API router
app.include_router(chat_router, prefix="/api", tags=["chat"])

@app.get("/", tags=["health"])
async def health_check():
    """A simple health check endpoint."""
    return {"status": "ok"}
