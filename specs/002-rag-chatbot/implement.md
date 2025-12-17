# Implementation: Integrated RAG Chatbot

**Status**: Final
**Author**: Gemini Agent
**Created**: 2025-12-17

## 1. Purpose of This Document

This document provides a high-level description of the implementation approach for the Integrated RAG Chatbot. It maps the actionable items from `tasks.md` to the architecture defined in `plan.md` and the requirements in `spec.md`. This is a descriptive guide to the solution, not a literal coding plan.

---

## 2. Backend Implementation (FastAPI)

The backend is a standalone FastAPI service located in the `rag-backend/` directory. Its responsibilities are strictly limited to data processing and query handling.

### 2.1. Data Preparation (Foundational)

This corresponds to **Phase 2** in `tasks.md`.

A series of Python scripts in `scripts/data_processing/` are executed to create the knowledge base.

1.  **Inventory**: The `inventory.py` script scans `my-Book/docs/` to create a manifest of all content files.
2.  **Chunking**: The `chunking.py` script reads the manifest, splits documents into manageable, semantically-aware chunks, and prepares them for embedding.
3.  **Embedding**: The `embedding.py` script takes the text chunks and uses the OpenAI API to generate vector embeddings for each one.
4.  **Storage**: The `storage.py` script loads the embeddings into the Qdrant vector database and their corresponding metadata (source file, chapter, etc.) into the Neon Postgres database. This is a one-time, offline process.

### 2.2. API Implementation

This corresponds to tasks in **Phases 3-5** of `tasks.md`.

-   **Service Initialization**: The FastAPI application is initialized in `rag-backend/app/main.py`, loading configuration from `rag-backend/core/config.py`.
-   **Query Endpoint**: A single `/query` endpoint in `main.py` handles all user-facing requests. It accepts a JSON payload containing the user's question and an optional `selected_text` field.
-   **General Query Flow**:
    1.  If `selected_text` is absent, the query is embedded.
    2.  The `retrieval.py` module queries the Qdrant database to find the most relevant text chunks.
    3.  The `orchestration.py` module constructs a prompt for the OpenAI LLM, injecting the retrieved chunks as context.
    4.  The LLM generates a response grounded in the provided context.
    5.  The response, along with source metadata from Postgres, is returned to the user.
-   **Selected-Text Flow**:
    1.  If `selected_text` is present, the vector search is bypassed entirely.
    2.  The `orchestration.py` module uses *only* the `selected_text` as context for the LLM prompt.
    3.  The LLM generates a response, which is returned to the user.

---

## 3. Frontend Implementation (Docusaurus)

The frontend consists of React components integrated into the existing Docusaurus site in the `my-Book/` directory.

### 3.1. UI Components

This corresponds to tasks in **Phases 3, 5, and 6** of `tasks.md`.

-   **Chat Components**: A suite of React components is created in `my-Book/src/components/Chatbot/`. This includes `ChatWindow.tsx` for the main interface, `ChatInput.tsx` for user input, and `ChatMessage.tsx` for displaying messages. The `ChatMessage.tsx` component is responsible for rendering source links when provided by the backend.
-   **Floating Button**: A `FloatingButton.tsx` component is created and integrated via `my-Book/src/theme/Root.tsx` to provide a persistent entry point for the chatbot. `Root.tsx` also manages the open/close state of the chat window.

### 3.2. Logic and Data Handling

This corresponds to tasks in **Phases 3 and 4** of `tasks.md`.

-   **API Integration**: An `api.ts` module handles all communication with the FastAPI backend. It manages the request/response cycle, including loading and error states.
-   **Text Selection**: The global `Root.tsx` component listens for `mouseup` events to detect when a user has selected text. This selected content is stored in a state that the `ChatWindow.tsx` component can access and send to the backend with a query.

---

## 4. Validation and Testing Approach

This corresponds to **Phase 7** in `tasks.md`.

-   **Functional Testing**: Manual execution of the user scenarios defined in `spec.md` to ensure both general and selected-text queries work as expected, including fallback and error states.
-   **Accuracy Verification**: A curated list of 20 questions is used to test the chatbot. The answers are manually compared against the source documents to ensure a 95% accuracy rate and to confirm no outside knowledge is used.
-   **Performance Testing**: Browser developer tools are used to measure the end-to-end response time for a set of sample queries to ensure the p90 latency is under 3 seconds.

---

## 5. Deployment & Integration

-   **Backend**: The FastAPI service in `rag-backend/` is containerized using Docker and deployed as a standalone web service. Environment variables for database and OpenAI credentials are injected at runtime.
-   **Frontend**: The new React components are part of the standard Docusaurus build process. When the `my-Book` site is built and deployed, the chatbot components are included as part of the static site's JavaScript bundle.

---

## 6. Documentation

-   **Prompt History Record (PHR)**: A final PHR is created in `history/prompts/002-rag-chatbot/` to document the successful implementation run and capture key outcomes for traceability.
