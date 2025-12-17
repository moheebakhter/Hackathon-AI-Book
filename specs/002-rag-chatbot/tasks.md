# Tasks: Integrated RAG Chatbot

**Input**: Design documents from `/specs/002-rag-chatbot/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Path Conventions

- **Backend**: `rag-backend/`
- **Frontend**: `my-Book/`
- **Data Scripts**: `scripts/data_processing/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization for the backend service.

- [ ] T001 Initialize FastAPI project in `rag-backend/`
- [ ] T002 Create directory structure `rag-backend/app`, `rag-backend/core`, `rag-backend/tests`
- [ ] T003 Configure environment variable handling in `rag-backend/core/config.py` using `.env` file

---

## Phase 2: Foundational (Data Pipeline)

**Purpose**: Core data ingestion pipeline that MUST be complete before any user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [ ] T004 [P] Implement content inventory script in `scripts/data_processing/inventory.py` to list all Markdown files in `my-Book/docs/`
- [ ] T005 [P] Implement content chunking script in `scripts/data_processing/chunking.py` to split documents into semantic chunks
- [ ] T006 [P] Implement embedding generation script in `scripts/data_processing/embedding.py` using OpenAI API
- [ ] T007 Implement data storage script in `scripts/data_processing/storage.py` to store vectors in Qdrant and metadata in Neon Postgres
- [ ] T008 Execute all data processing scripts to populate databases

**Checkpoint**: Foundation ready - databases are populated and ready for querying.

---

## Phase 3: User Story 1 - Book-Based Q&A (Priority: P1) 🎯 MVP

**Goal**: A user can ask a question in a chat interface and receive an answer based on the entire book's content.

**Independent Test**: The backend service can take a JSON query, retrieve context from Qdrant, generate an answer with the LLM, and return it. The frontend can send a query and display the result.

### Implementation for User Story 1

- [ ] T009 [US1] Implement a `/query` endpoint in `rag-backend/app/main.py`
- [ ] T010 [US1] Implement the retrieval pipeline to search Qdrant in `rag-backend/app/retrieval.py`
- [ ] T011 [US1] Implement LLM prompt construction and response generation in `rag-backend/app/orchestration.py`
- [ ] T012 [P] [US1] Create a basic chat input component in `my-Book/src/components/Chatbot/ChatInput.tsx`
- [ ] T013 [P] [US1] Create a basic message display component in `my-Book/src/components/Chatbot/ChatMessage.tsx`
- [ ] T014 [US1] Implement the main chat window component in `my-Book/src/components/Chatbot/ChatWindow.tsx`
- [ ] T015 [US1] Create an API client service to communicate with the backend in `my-Book/src/components/Chatbot/api.ts`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Selected-Text-Only Q&A (Priority: P1)

**Goal**: A user can highlight text on a page and ask a question specifically about that selection.

**Independent Test**: The frontend can capture highlighted text and send it with a query. The backend correctly bypasses vector search and uses only the provided text for context.

### Implementation for User Story 2

- [ ] T016 [US2] Modify `/query` endpoint in `rag-backend/app/main.py` to accept optional `selected_text` field and route to a different logic path if present.
- [ ] T017 [US2] Implement the selection-only response logic in `rag-backend/app/orchestration.py`
- [ ] T018 [P] [US2] Implement a global text selection listener in `my-Book/src/theme/Root.tsx` (or equivalent global component).
- [ ] T019 [US2] Add a "Ask about selection" button to the `my-Book/src/components/Chatbot/ChatWindow.tsx` that appears when text is selected.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Source-Grounded Responses (Priority: P2)

**Goal**: All answers for general book questions are accompanied by clickable citations to the source material.

**Independent Test**: The backend response for a general query includes source metadata. The frontend correctly parses and displays this metadata as a clickable link.

### Implementation for User Story 3

- [ ] T020 [US3] Modify the backend response model for `/query` in `rag-backend/app/main.py` to include a `sources` array.
- [ ] T021 [US3] Ensure the retrieval pipeline in `rag-backend/app/retrieval.py` fetches and returns source metadata (file path) along with content chunks.
- [ ] T022 [US3] Update the `my-Book/src/components/Chatbot/ChatMessage.tsx` component to display source links when present in the API response.

**Checkpoint**: General query responses now include source links.

---

## Phase 6: User Story 4 - Embedded UI Experience (Priority: P2)

**Goal**: The chatbot is accessible via a non-intrusive, persistent floating action button on all documentation pages.

**Independent Test**: A floating button is visible on all doc pages. Clicking it toggles the visibility of the chat window.

### Implementation for User Story 4

- [ ] T023 [P] [US4] Create a floating action button component in `my-Book/src/components/Chatbot/FloatingButton.tsx`
- [ ] T024 [US4] Add the `FloatingButton` and `ChatWindow` components to `my-Book/src/theme/Root.tsx` and manage the open/close state.

**Checkpoint**: The full chatbot UI is embedded and functional across the site.

---

## Phase 7: Polish & Validation

**Purpose**: Final validation, documentation, and cleanup.

- [ ] T025 [P] Perform functional testing for all user stories as per `spec.md`.
- [ ] T026 [P] Manually verify accuracy for 20 test questions as per `spec.md`.
- [ ] T027 Measure p90 latency to validate performance success criteria from `spec.md`.
- [ ] T028 Create a final Prompt History Record (PHR) for the implementation in `history/prompts/002-rag-chatbot/`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can start immediately.
- **Foundational (Phase 2)**: Depends on Setup. Blocks all user stories.
- **User Stories (Phase 3-6)**: Depend on Foundational.
- **Polish (Phase 7)**: Depends on all user stories being complete.

### User Story Dependencies

- **US1**: Can start after Foundational.
- **US2**: Depends on US1 (shares UI and backend endpoint).
- **US3**: Depends on US1 (enhances the response from US1).
- **US4**: Depends on US1 (provides the container for the US1 UI).

### Implementation Strategy

1.  Complete Phase 1 (Setup) and Phase 2 (Foundational).
2.  Implement all tasks for User Story 1 to create the MVP.
3.  Incrementally add User Stories 2, 3, and 4.
4.  Complete Phase 7 (Validation).
