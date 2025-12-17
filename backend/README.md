# RAG Chatbot Backend

This directory contains the backend service for the Integrated RAG Chatbot.

## Stack

- **Framework**: FastAPI
- **Vector Database**: Qdrant
- **Metadata Store**: Neon Serverless Postgres
- **LLM**: OpenAI
- **Package Manager**: uv

## Setup

1.  Create a `.env` file in the `backend/` root directory with the following variables:

    ```
    OPENAI_API_KEY=...
    QDRANT_URL=...
    QDRANT_API_KEY=...
    DATABASE_URL=...
    ```

2.  Install dependencies:
    ```sh
    uv pip sync
    ```

3.  Run the development server:
    ```sh
    uv run uvicorn src.main:app --reload
    ```

The API will be available at `http://127.0.0.1:8000`.
