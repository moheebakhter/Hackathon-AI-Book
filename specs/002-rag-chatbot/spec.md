# Feature: Integrated RAG Chatbot

**Version**: 1.0
**Status**: Final
**Author**: Gemini Agent
**Created**: 2025-12-17
**Last Updated**: 2025-12-17

## 1. Overview

This document specifies the requirements for an integrated Retrieval-Augmented Generation (RAG) chatbot. The chatbot is embedded within the "Physical AI & Humanoid Robotics Book" Docusaurus website. Its primary purpose is to provide users with an interactive way to query and understand the book's content, delivering accurate, context-aware answers grounded exclusively in the provided text.

## 2. Goals

- **Accurate Information Retrieval**: Answer user questions using only the content available within the book's pages.
- **Contextual Querying**: Allow users to highlight specific text on a page and ask questions based solely on that selection.
- **Hallucination Prevention**: Ensure all answers are directly traceable to source material within the book, preventing the model from inventing information.
- **Seamless Integration**: Embed the chatbot into the Docusaurus UI in a way that feels native and intuitive to the user experience.

## 3. Architecture Constraints

The development of this feature must adhere to the following architectural decisions:

- **Frontend**: The chatbot's user interface must be implemented as React components within the existing Docusaurus application located at `my-Book/`.
- **Backend**: All backend services must be built using FastAPI and reside in a new, separate folder at the project root. No backend code is permitted inside the `my-Book/` directory.
- **LLM Provider**: The core language model interactions will be handled via the OpenAI Agents / ChatKit SDK.
- **Vector Database**: Embeddings and vector search will be managed by a Qdrant Cloud (Free Tier) instance.
- **Metadata Database**: A Neon Serverless Postgres instance will be used for storing metadata associated with content chunks.

## 4. Non-Goals

- The chatbot will **not** answer questions using information from outside the book's content.
- The chatbot will **not** maintain a conversational memory or history across multiple distinct queries. Each question is treated as a standalone interaction.
- The chatbot will **not** support user accounts, personalization, or saving chat history.
- The chatbot will **not** have the ability to navigate the Docusaurus site on behalf of the user.

## 5. User Scenarios & Testing

### P1: Book-Based Question Answering

- **Description**: A user asks a general question about a topic covered in the book, and the chatbot provides an answer based on the entire book's content.
- **Why this priority**: This is the core functionality of the RAG chatbot and represents the primary value proposition for users seeking information.
- **Independent Test**: The system can successfully receive a question, retrieve relevant context from the vector database, and generate a correct, source-grounded answer.
- **Acceptance Scenarios**:
    - **Given** a user is on any page of the book
    - **When** they open the chatbot and ask, "What is ROS2?"
    - **Then** the chatbot returns a concise summary of ROS2 based on content from `module-1-ros2/ros-architecture.md`.
    - **And** the response includes a citation pointing to the source page.

### P1: Selected-Text-Only Question Answering

- **Description**: A user highlights a specific paragraph or section on a page and asks a clarifying question about that selection.
- **Why this priority**: This provides a powerful, highly contextual way for users to drill down into specific details without the ambiguity of a general search.
- **Independent Test**: The system can accept a user's text selection and a related question, and generate an answer using *only* the selected text as context.
- **Acceptance Scenarios**:
    - **Given** a user is viewing the `urdf-for-humanoids.md` page
    - **When** they highlight a paragraph describing the `<joint>` element and ask, "What does the 'type' attribute do?"
    - **Then** the chatbot provides an answer explaining the 'type' attribute using only information from the selected paragraph.
    - **And** the response does not draw from any other part of the book.

### P2: Source-Grounded Responses

- **Description**: All answers provided by the chatbot must be accompanied by clear, clickable citations that link directly to the source page and section within the book.
- **Why this priority**: Citations build user trust and verify that the chatbot's answers are grounded in the book's content, fulfilling the core promise of RAG.
- **Independent Test**: For any generated answer, the system provides one or more valid source links that, when clicked, navigate the user to the relevant content.
- **Acceptance Scenarios**:
    - **Given** the chatbot has generated an answer to a question
    - **When** the user inspects the response
    - **Then** a "Source" link is visible with the response.
    - **And** clicking the link navigates the user to the correct source page within the book.

### P2: Embedded UI Experience

- **Description**: The chatbot is accessible via a non-intrusive, persistent floating action button on all documentation pages.
- **Why this priority**: Easy and consistent access is crucial for user adoption. The chatbot should feel like a part of the site, not an external tool.
- **Independent Test**: A floating chatbot icon is present on all `/docs/` pages, and clicking it opens the chat interface in a chat overlay.
- **Acceptance Scenarios**:
    - **Given** a user is viewing any documentation page
    - **When** the page loads
    - **Then** a chatbot icon is visible in the bottom-right corner of the viewport.
    - **And** clicking the icon opens a chat window overlay without navigating away from the current page.

## 6. Data & Retrieval Rules

- **Book-Only Embeddings**: The embedding process will be strictly limited to the Markdown files (`.md`, `.mdx`) within the `my-Book/docs/` directory. No other content will be indexed.
- **Chunk Metadata**: Each content chunk stored in the vector database will be associated with metadata in the Postgres database, including the source file path, chapter, and section heading.
- **Scoped Retrieval**: Queries based on user-selected text **must** bypass the global vector search. The LLM will only use the user-provided text as its context for these queries.
- **Graceful Failure**: If a user's question yields no relevant context from the vector search after applying a similarity score threshold, the chatbot must not attempt to answer. It will respond with the message: "I'm sorry, I couldn't find any relevant information on that topic in the book."

## 7. Success Criteria

The feature will be considered successful when the following criteria are met:

- **Accuracy**: At least 19 out of 20 answers (95%) are factually correct and directly supported by the book's content, as verified by manual review of 20 representative test questions covering all main book modules.
- **Relevance**: For general queries, the top 3 retrieved context chunks are relevant to the user's question in at least 90% of tested cases.
- **Performance**: The p90 end-to-end response time (from submitting a question to receiving an answer) is less than 3 seconds.
- **Usability**: A first-time user can successfully complete both a general and a selected-text query within 60 seconds of opening the interface without instructions.

## 8. Deliverables

- `specs/002-rag-chatbot/spec.md` (this document)
- `specs/002-rag-chatbot/plan.md`
- `specs/002-rag-chatbot/tasks.md`
- `specs/002-rag-chatbot/implement.md`

## 9. Constraints

- This work must not modify any specifications, plans, or code related to the Part-1 book content feature (`001-humanoid-robotics-book`).
- This specification must be self-contained and provide all necessary information for a developer to proceed to the planning phase without referencing external conversations or documents.