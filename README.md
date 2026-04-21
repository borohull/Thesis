# ELTE Informatics Chatbot

A local, privacy-preserving RAG (Retrieval-Augmented Generation) chatbot for the ELTE Faculty of Informatics. It answers student and staff questions about curriculum, prerequisites, exam rules, and registration using content crawled from official ELTE sources. The entire stack runs offline: a local LLM via Ollama, embeddings via sentence-transformers, and a ChromaDB vector store, served through a FastAPI backend.

## Features

- **Fully local** — no external API calls; all inference and retrieval happen on your machine.
- **RAG pipeline** — retrieves the top-K relevant chunks from ChromaDB and grounds the LLM answer in cited sources.
- **Multi-format ingestion** — HTML, PDF, and DOCX documents crawled via BFS from ELTE websites.
- **Incremental ingestion** — SHA-256 manifest avoids re-embedding unchanged documents.
- **User file uploads** — attach documents to a chat session for ad-hoc Q&A.
- **Runtime model switching** — swap between Ollama models (e.g. `llama3.2:3b`, `gemma3:4b`) from the UI.
- **Session history** — persistent chats with delete support.
- **SQLite logging** — every query, retrieval, and response is logged for evaluation.
- **Minimal web UI** — self-contained HTML/JS frontend with ELTE brand styling.

## Architecture

```
Browser ──► FastAPI (app/) ──► ChromaDB (data/processed/chroma_db/)
                      └─────► Ollama (localhost:11434)
```

**Data pipeline** (one-time, build the vector store):

1. `scripts/crawler.py` — BFS crawl of ELTE sites → `data/raw/` (HTML, PDF, DOCX)
2. `notebooks/01_data_ingestion.ipynb` — load + chunk documents → `data/processed/chunks.json`
3. `notebooks/02_embedding.ipynb` — encode chunks → ChromaDB `elte_ik` collection
4. `notebooks/03_RAG_pipeline.ipynb` — end-to-end RAG sanity check

**Serving pipeline** (FastAPI):

- `app/settings.py` — config constants (paths, model names, `TOP_K`, temperature)
- `app/rag.py` — ChromaDB + SentenceTransformer singletons; `retrieve()`, `build_prompt()`, `call_ollama()`, `rag_query()`
- `app/main.py` — REST endpoints (`/chat`, `/health`, uploads, sessions, models)
- `app/logger.py` — SQLite logging to `data/logs/chat_logs.db`
- `app/static/index.html` — chat UI

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) running locally
- At least one Ollama model pulled:
  ```bash
  ollama pull llama3.2:3b
  ```

## Installation

```bash
git clone <repo-url>
cd elte_chat
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### Run the API server

```bash
uvicorn app.main:app --reload
```

The server starts at `http://localhost:8000`. The chat UI is available at `http://localhost:8000/static/index.html`.

### CLI client

```bash
python scripts/chat_cli.py
```

Requires the FastAPI server to be running.

### Build the vector store

```bash
# 1. Crawl ELTE sources (resumable; --reset to start fresh)
python scripts/crawler.py

# 2. Run the ingestion notebooks in order
#    notebooks/01_data_ingestion.ipynb
#    notebooks/02_embedding.ipynb
#    notebooks/03_RAG_pipeline.ipynb
```

## Configuration

All tunable parameters live in `app/settings.py`:

| Setting           | Default                     | Notes                                                   |
| ----------------- | --------------------------- | ------------------------------------------------------- |
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2`          | Must match the model used in `02_embedding.ipynb`       |
| `COLLECTION_NAME` | `elte_ik`                   | ChromaDB collection name                                |
| `TOP_K`           | `3`                         | Chunks retrieved per query                              |
| `OLLAMA_MODEL`    | `llama3.2:3b`               | Must be pulled in Ollama                                |
| `TEMPERATURE`     | `0.1`                       | Low = factual, less hallucination                       |
| `CHROMA_PATH`     | `data/processed/chroma_db`  | Relative to project root                                |

## Evaluation

`notebooks/04_evaluation.ipynb` benchmarks four configurations against 20 test questions (15 in-scope, 5 out-of-scope):

| Config | Model         | Retrieval |
| ------ | ------------- | --------- |
| A1     | `llama3.2:3b` | No RAG    |
| B1     | `llama3.2:3b` | RAG (top-5) |
| A2     | `gemma3:4b`   | No RAG    |
| B2     | `gemma3:4b`   | RAG (top-5) |

Metrics: ROUGE-L, faithfulness (chunk overlap), refusal rate on out-of-scope queries, retrieval hit-rate, and response time. Results are written to `data/evaluation/`.

## Project Structure

```
elte_chat/
├── app/                    # FastAPI backend
│   ├── main.py             # API endpoints
│   ├── rag.py              # retrieval + generation
│   ├── settings.py         # configuration
│   ├── logger.py           # SQLite logging
│   └── static/             # web UI
├── scripts/
│   ├── crawler.py          # BFS web crawler
│   └── chat_cli.py         # terminal client
├── notebooks/              # data pipeline + evaluation
├── data/
│   ├── raw/                # crawled source files
│   ├── processed/          # chunks.json + ChromaDB
│   ├── logs/               # chat_logs.db
│   └── evaluation/         # benchmark results
└── requirements.txt
```

## Key Constraints

- **Embedding model consistency** — `settings.EMBEDDING_MODEL` must match the model used when building the ChromaDB index. Changing it requires re-running `02_embedding.ipynb`.
- **Ollama must be running** — `/health` reports its status; `/chat` will error if Ollama is down.
- **Run from the project root** — paths in `settings.py` are relative to the repo root.

## License

Academic thesis project — ELTE Faculty of Informatics.
