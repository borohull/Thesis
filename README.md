# ELTE IK Assistant

A locally deployed retrieval-augmented generation (RAG) chatbot for the **ELTE Faculty of Informatics**. Students and staff can ask natural-language questions about the curriculum, course prerequisites, exam rules, and Neptun registration procedures — and receive answers grounded in official faculty documents, with no data ever leaving the machine.

---

## Features

- **Fully offline** — after initial setup, no internet connection is required
- **Privacy-safe** — no query, retrieved chunk, or generated answer leaves the host machine
- **RAG pipeline** — answers are grounded in crawled faculty documents, not model guesswork
- **Two local models** — `llama3.2:3b` and `gemma3:4b` served via Ollama
- **Source references** — every answer links back to the documents it used
- **Session history** — conversations persist across browser refreshes and server restarts
- **Document upload** — extend the knowledge base at runtime with your own PDFs, HTML, or DOCX files
- **REST API** — all functionality exposed via a clean HTTP API
- **CLI client** — terminal interface for scripting and testing
- **Docker support** — one command to run the full stack

---

## Tech Stack

| Component | Role |
|---|---|
| [Ollama](https://ollama.com) | Local LLM server |
| `llama3.2:3b` / `gemma3:4b` | Language models (4-bit quantised) |
| `all-MiniLM-L6-v2` | Sentence embedding model |
| [ChromaDB](https://www.trychroma.com) | Vector store |
| [FastAPI](https://fastapi.tiangolo.com) | Backend REST API |
| SQLite | Interaction logging |
| Vanilla JavaScript | Single-page frontend |
| Docker Compose | Containerised deployment |

---

## System Requirements

| Component | Requirement |
|---|---|
| OS | Windows 10/11, macOS 12+, or Ubuntu 22.04+ |
| RAM | 8 GB minimum (16 GB recommended) |
| Disk | ~6 GB (models + vector store + crawled data) |
| GPU | Not required — CPU-only inference |
| Internet | Required during first-run setup only |

---

## Installation

### Option A — Docker (recommended for shared/server deployments)

```bash
git clone https://github.com/borohull/Thesis.git
cd Thesis/elte_chat
docker compose up -d
```

On first run, the container crawls ELTE documents and builds the vector index before starting — allow **5–10 minutes**. Monitor progress with:

```bash
docker compose logs -f app
```

Wait for `Application startup complete`, then open:

```
http://localhost:8000/static/index.html
```

To stop:
```bash
docker compose down
```

---

### Option B — Manual Setup

**Prerequisite:** Python 3.10+ must be installed.

**1. Install Ollama and pull models**
```bash
ollama serve
ollama pull llama3.2:3b
ollama pull gemma3:4b
```

**2. Clone the repository**
```bash
git clone https://github.com/borohull/Thesis.git
cd Thesis/elte_chat
```

**3. Run the setup script**

macOS / Linux:
```bash
chmod +x setup.sh
./setup.sh
```

Windows:
```bash
setup.bat
```

The script creates a virtual environment, installs dependencies, crawls ELTE documents, and builds the vector index. First run takes approximately **5–10 minutes**.

**4. Start the server**

macOS / Linux:
```bash
source .venv/bin/activate && uvicorn app.main:app
```

Windows:
```bash
.venv\Scripts\activate && uvicorn app.main:app
```

**5. Open the interface**
```
http://localhost:8000/static/index.html
```

Verify the server is running:
```bash
curl http://localhost:8000/health
# Expected: {"status": "ok", "ollama": true}
```

---

## Usage

### Web Interface

The interface has three panels:

- **Left sidebar** — chat session history; click to resume, or start a **New chat**
- **Centre panel** — type questions and read answers with source references
- **Right sidebar** — model selector, connectivity status, knowledge base size, uploaded documents

**Asking questions** — questions should relate to the ELTE Faculty of Informatics: curriculum, regulations, procedures, and student services. Typical response time on CPU-only hardware is 40–70 seconds.

**Source references** — every answer shows which documents were used. Click a filename to open the original source.

**Uploading documents** — click **Upload document** above the input field and select a PDF, HTML, or DOCX file (max 20 MB). The file is indexed immediately with no server restart required.

### Command-Line Client

```bash
python scripts/chat_cli.py
```

Available commands inside the client:

| Command | Description |
|---|---|
| `/sessions` | List all past sessions |
| `/resume` | Resume a previous session |
| `/model` | Switch the active language model |
| `/session` | Show current session name and model |
| `/commands` | Show help |
| `exit` / `quit` | Quit the client |

---

## API Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/health` | Server and Ollama status |
| `GET` | `/models` | Available Ollama models |
| `GET` | `/info` | Active model, chunk count, uploaded files |
| `POST` | `/chat` | Submit a question, get a grounded answer |
| `GET` | `/sessions` | List all sessions |
| `GET` | `/sessions/{id}/messages` | Messages in a session |
| `DELETE` | `/sessions/{id}` | Delete a session |
| `POST` | `/upload` | Upload and index a document |
| `GET` | `/source/{filename}` | Serve the original source file |

---

## Project Structure

```
elte_chat/
├── app/
│   ├── settings.py       # All tunable parameters in one place
│   ├── rag.py            # Retrieval, prompt construction, Ollama call
│   ├── ingest.py         # Chunking and embedding for uploaded files
│   ├── logger.py         # SQLite interaction logging
│   ├── main.py           # FastAPI entry point and HTTP endpoints
│   └── static/           # Single-page HTML/CSS/JS frontend
├── scripts/
│   ├── crawler.py        # BFS web crawler for ELTE documents
│   ├── build_index.py    # Chunking, embedding, ChromaDB upsert
│   └── chat_cli.py       # Terminal client
├── tests/                # End-to-end pytest suite (16 test cases)
├── data/
│   ├── raw/              # Crawled HTML, PDF, DOCX files
│   ├── processed/        # ChromaDB vector store + manifest
│   ├── logs/             # SQLite chat log
│   └── uploads/          # User-uploaded documents
├── setup.sh / setup.bat  # First-run setup scripts
└── docker-compose.yml    # Full-stack container orchestration
```

---

## Configuration

All parameters are in `app/settings.py`. Key settings:

| Parameter | Default | Description |
|---|---|---|
| `OLLAMA_MODEL` | `llama3.2:3b` | Default language model |
| `TOP_K` | `5` | Chunks retrieved per query |
| `CHUNK_SIZE` | `800` | Max chunk size in characters |
| `CHUNK_OVERLAP` | `150` | Overlap between adjacent chunks |
| `TEMPERATURE` | `0.1` | LLM sampling temperature |
| `TIMEOUT_S` | `120` | Per-request Ollama timeout (seconds) |
| `MAX_UPLOAD_BYTES` | `20 MB` | Max upload file size |

Switching models requires only changing `OLLAMA_MODEL`. Changing `EMBEDDING_MODEL` requires rebuilding the vector store.

---

## Running the Tests

Requires Ollama running, `llama3.2:3b` pulled, and the FastAPI server started.

```bash
python -m pytest tests
```

All 16 end-to-end test cases cover health checks, chat responses, session management, document upload, and system info endpoints. Tests are automatically skipped (not failed) if the server or Ollama is unreachable.

---

## Evaluation Results

Evaluated across four configurations on CPU-only hardware (Intel Core i5-10300H, 8 GB RAM, no GPU):

| Config | Model | RAG | ROUGE-L | Sem Sim | Refusal | Avg Latency |
|---|---|---|---|---|---|---|
| A1 | `llama3.2:3b` | No | 0.128 | 0.631 | 0% | 41.5 s |
| B1 | `llama3.2:3b` | Yes | 0.319 | 0.757 | 80% | 53.2 s |
| A2 | `gemma3:4b` | No | 0.076 | 0.618 | 0% | 157.2 s |
| **B2** | **`gemma3:4b`** | **Yes** | **0.357** | **0.778** | **100%** | **66.9 s** |

**Recommended configuration: `gemma3:4b` with RAG (B2)** — highest answer quality, perfect out-of-scope refusal, and lower latency than its own no-RAG baseline.

RAG adds 2.5× ROUGE-L improvement for Llama and 4.7× for Gemma. Without RAG, neither model reliably answers ELTE-specific questions.

---

## Limitations

- Response latency exceeds the 30-second target on CPU-only hardware. A GPU deployment would resolve this.
- Retrieval hit-rate is 0.933 (14/15 in-scope questions). One question on Stipendium Hungaricum + Erasmus eligibility was missed due to shallow navigation text not chunking well.
- The prompt-level refusal mechanism is not fully robust — a score-based threshold is a planned improvement.
- The 20-question evaluation benchmark is narrow; broader coverage is needed.

---

## Author

**Ulziibayar Borokhul**  
Computer Science BSc — Eötvös Loránd University, Faculty of Informatics  
Supervisor: Altangerel Gereltsetseg, Assistant Professor, Ph.D  
Budapest, 2026