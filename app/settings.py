from pathlib import Path

BASE_DIR             = Path(__file__).parent.parent
CHROMA_PATH          = str(BASE_DIR / "data/processed/chroma_db")
CHUNKS_PATH          = str(BASE_DIR / "data/processed/chunks.json")
MANIFEST_PATH        = str(BASE_DIR / "data/processed/manifest.json")
PENDING_CHANGES_PATH = str(BASE_DIR / "data/processed/pending_changes.json")
RAW_DIR              = str(BASE_DIR / "data/raw")
UPLOAD_DIR           = str(BASE_DIR / "data/uploads")
COLLECTION_NAME      = "elte_ik"
EMBEDDING_MODEL      = "all-MiniLM-L6-v2"
TOP_K                = 5
CHUNK_SIZE           = 800
CHUNK_OVERLAP        = 150
MAX_UPLOAD_BYTES     = 20 * 1024 * 1024  # 20 MB
ALLOWED_UPLOAD_TYPES = {
    "application/pdf",
    "text/html",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/msword",      
    "application/octet-stream", 
}
ALLOWED_EXTENSIONS = {".pdf", ".html", ".htm", ".docx"}

OLLAMA_URL      = "http://localhost:11434/api/generate"
OLLAMA_MODEL    = "gemma3:4b"
TEMPERATURE     = 0.1
TIMEOUT_S       = 120
