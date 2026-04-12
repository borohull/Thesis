# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Local RAG-based chatbot for ELTE Faculty of Informatics. Answers student/staff questions about curriculum, prerequisites, exam rules, and registration. Runs entirely offline using a local LLM (Ollama) + ChromaDB + FastAPI.

## Development Commands

### Prerequisites
- Ollama running locally with `llama3.2:3b` pulled: `ollama pull llama3.2:3b`
- Python virtualenv with dependencies: `pip install -r requirements.txt`

### Run the API server
```bash
uvicorn app.main:app --reload
```
The server starts on `http://localhost:8000`. The chat UI is served at `http://localhost:8000/static/index.html`.

### Run the CLI client
```bash
python scripts/chat_cli.py
```
Requires the FastAPI server to be running.

### Run the data pipeline (one-time setup)
```bash
# Step 1: Crawl ELTE websites (downloads to data/raw/)
python crawler.py
# Reset and re-crawl: python crawler.py --reset

# Step 2-4: Run notebooks in order
# 01_data_ingestion.ipynb  → produces data/processed/chunks.json
# 02_embedding.ipynb       → populates data/processed/chroma_db/
# 03_RAG_pipeline.ipynb    → end-to-end RAG test
```

## Architecture

```
Browser → FastAPI (app/) → ChromaDB (data/processed/chroma_db/) + Ollama (localhost:11434)
```

**Data pipeline** (run once to build the vector store):
1. `crawler.py` — BFS crawl of ELTE sites → `data/raw/` (HTML, PDF, DOCX)
2. `notebooks/01_data_ingestion.ipynb` — loads/chunks documents → `data/processed/chunks.json`
3. `notebooks/02_embedding.ipynb` — encodes chunks → ChromaDB `elte_ik` collection (6112 docs, 384-dim)

**Serving pipeline** (FastAPI):
- `app/settings.py` — all config constants (paths, model names, TOP_K, temperature)
- `app/rag.py` — singletons for ChromaDB client + SentenceTransformer; `retrieve()`, `build_prompt()`, `call_ollama()`, `rag_query()`
- `app/main.py` — `POST /chat` calls `rag_query()`; `GET /health` checks Ollama
- `app/logger.py` — SQLite logging of all interactions to `data/logs/chat_logs.db`
- `app/static/index.html` — self-contained chat UI (vanilla JS, ELTE brand colors)

## Configuration

All tunable parameters live in `app/settings.py`:

| Setting | Default | Notes |
|---|---|---|
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | Used in both notebook 02 and `rag.py` — must match |
| `COLLECTION_NAME` | `elte_ik` | ChromaDB collection |
| `TOP_K` | `3` | Chunks retrieved per query |
| `OLLAMA_MODEL` | `llama3.2:3b` | Must be pulled in Ollama |
| `TEMPERATURE` | `0.1` | Low = factual, less hallucination |
| `CHROMA_PATH` | `data/processed/chroma_db` | Relative to project root |

## Evaluation

`notebooks/05_evaluation.ipynb` benchmarks two configs against 20 test questions (15 in-scope, 5 out-of-scope):
- **Config A**: Raw Ollama (no RAG)
- **Config B**: RAG with top-3 chunks

Metrics: ROUGE-L, faithfulness (chunk overlap), refusal rate (out-of-scope), response time. Results saved to `data/evaluation/`.

## Feature Planning

Whenever a plan for a new feature or significant change is devised, save it as a markdown file in `.claude/plans/` using this format:

**Filename:** `.claude/plans/YYYY-MM-DD_<feature-slug>.md`
Example: `.claude/plans/2026-04-09_reranking-pipeline.md`

**File structure:**
```markdown
# <Feature Name>

**Date:** YYYY-MM-DD

## Goal
One-sentence description of what this feature achieves.

## Plan
Step-by-step implementation plan.

## Notes
Any constraints, open questions, or decisions made.
```

Create the `.claude/plans/` directory if it doesn't exist. Do this before beginning implementation, not after.

## Key Constraints

- **Embedding model must be consistent**: `settings.EMBEDDING_MODEL` must match what was used in `02_embedding.ipynb` to build the ChromaDB index. Changing it requires re-running notebook 02.
- **Ollama must be running**: The API server fails gracefully if Ollama is down (`/health` reports it), but `/chat` will error.
- **Paths are relative to project root**: Run `uvicorn` from the repo root, not from `app/`.
