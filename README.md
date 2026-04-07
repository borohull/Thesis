# ELTE Informatics Chatbot

A local RAG-based chatbot for the ELTE Faculty of Informatics. Answers student and staff questions about curriculum, prerequisites, exam rules, registration, and other faculty-related information using a small local language model — no cloud APIs required.

Built as a BSc thesis project.

## Architecture

```
                  Browser (index.html)
                         |
                    POST /chat
                         |
                   FastAPI Backend
                   /            \
           ChromaDB              Ollama
        (vector search)       (llama3.2:3b)
              |
        Embedded Chunks
     (all-MiniLM-L6-v2)
```

**Query flow:** User question → retrieve top-K similar document chunks from ChromaDB → build context-aware prompt → send to local LLM via Ollama → return answer with source citations.

## Project Structure

```
elte_chat/
├── app/
│   ├── main.py              # FastAPI server (/chat, /health)
│   ├── rag.py               # RAG pipeline (retrieve, prompt, call LLM)
│   ├── settings.py          # Configuration constants
│   ├── logger.py            # SQLite chat logging
│   └── static/
│       └── index.html       # Chat UI (self-contained)
├── notebooks/
│   ├── 01_data_ingestion.ipynb   # Load & chunk documents
│   ├── 02_embedding.ipynb        # Generate embeddings → ChromaDB
│   ├── 03_RAG_pipeline.ipynb     # End-to-end RAG testing
│   └── 05_evaluation.ipynb       # Evaluation (ROUGE-L, faithfulness)
├── scripts/
│   └── chat_cli.py          # CLI chat client
├── crawler.py               # Web crawler for ELTE sites
├── data/
│   ├── raw/                 # Crawled HTML, PDFs, DOCX (gitignored)
│   ├── processed/           # chunks.json + chroma_db/ (gitignored)
│   └── logs/                # SQLite chat logs
└── requirements.txt
```

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python, FastAPI, Uvicorn |
| LLM | Ollama (llama3.2:3b, local) |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2, 384-dim) |
| Vector DB | ChromaDB (persistent, cosine similarity) |
| Document loading | LangChain, PyMuPDF, BeautifulSoup, python-docx |
| Web crawler | httpx, BeautifulSoup |
| Frontend | Vanilla HTML/CSS/JS |
| Logging | SQLite |

## Setup

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.ai/) installed and running

### Installation

```bash
# Clone the repo
git clone https://github.com/borohull/elte_chat.git
cd elte_chat

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Pull the LLM
ollama pull llama3.2:3b
```

### Data Pipeline

Run the notebooks in order to build the knowledge base:

```bash
# 1. Crawl ELTE websites
python crawler.py --reset

# 2. Open Jupyter and run notebooks sequentially
jupyter notebook notebooks/
```

- **01_data_ingestion.ipynb** — Loads crawled files (HTML, PDF, DOCX), cleans text, splits into chunks, saves to `data/processed/chunks.json`
- **02_embedding.ipynb** — Encodes chunks with sentence-transformers, upserts into ChromaDB
- **03_RAG_pipeline.ipynb** — Tests the full retrieve → prompt → answer pipeline

### Run the App

```bash
# Start Ollama (if not already running)
ollama serve

# Start the backend
uvicorn app.main:app --reload

# Open the chat UI
# http://localhost:8000/static/index.html
```

## Crawler

The crawler recursively scrapes English-language pages from ELTE websites:

- **inf.elte.hu/en/** — Full Faculty of Informatics site
- **www.elte.hu/en/** — 20 whitelisted student-focused pages (housing, finances, visa, etc.)

```bash
python crawler.py              # Resumable — skips already-downloaded pages
python crawler.py --reset      # Wipe data/raw/ and data/processed/, then crawl fresh
```

Features:
- BFS crawl with 0.5s politeness delay
- English-only filtering (URL path, `<html lang>`, `<meta>` tag)
- Automatic PDF and DOCX download from discovered links
- Domain-mirrored folder structure in `data/raw/`

## Evaluation

The evaluation notebook (`05_evaluation.ipynb`) tests the system on 20 faculty-specific questions, comparing:

| Config | Description |
|--------|------------|
| A | Raw Ollama (no RAG) |
| B | RAG-augmented |
| C | RAG + fine-tuned (placeholder) |

Metrics: ROUGE-L, faithfulness (chunk overlap), refusal rate, response time.

## Configuration

Key settings in `app/settings.py`:

```python
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
OLLAMA_MODEL    = "llama3.2:3b"
TOP_K           = 3
TEMPERATURE     = 0.1
```
