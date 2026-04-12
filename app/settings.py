from pathlib import Path

BASE_DIR             = Path(__file__).parent.parent
CHROMA_PATH          = str(BASE_DIR / "data/processed/chroma_db")
CHUNKS_PATH          = str(BASE_DIR / "data/processed/chunks.json")
MANIFEST_PATH        = str(BASE_DIR / "data/processed/manifest.json")
PENDING_CHANGES_PATH = str(BASE_DIR / "data/processed/pending_changes.json")
RAW_DIR              = str(BASE_DIR / "data/raw")
COLLECTION_NAME      = "elte_ik"
EMBEDDING_MODEL      = "all-MiniLM-L6-v2"
TOP_K                = 3

OLLAMA_URL      = "http://localhost:11434/api/generate"
OLLAMA_MODEL    = "llama3.2:3b"
TEMPERATURE     = 0.1
TIMEOUT_S       = 120
