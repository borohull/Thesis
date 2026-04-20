import hashlib
import re
import time
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app import ingest
from app.logger import (
    delete_session,
    get_session_messages,
    get_sessions,
    init_db,
    log_chat,
    log_upload,
    upsert_session,
)
from app.rag import check_ollama, rag_query
from app.settings import (
    ALLOWED_EXTENSIONS, ALLOWED_UPLOAD_TYPES, EMBEDDING_MODEL,
    MAX_UPLOAD_BYTES, OLLAMA_MODEL, RAW_DIR, UPLOAD_DIR,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="ELTE IK Chatbot", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")


class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None
    model: str | None = None


class ChatResponse(BaseModel):
    answer: str
    sources: list[dict]
    response_ms: int


class UploadResponse(BaseModel):
    status: str        # "indexed" | "already_indexed"
    file_name: str
    sha256: str
    chunk_count: int
    collection_size: int


class SessionSummary(BaseModel):
    session_id: str
    title: str
    created_at: str
    updated_at: str


class SessionMessage(BaseModel):
    user_message: str
    answer: str
    sources: list[dict]
    timestamp: str


@app.get("/health")
def health():
    return {"status": "ok", "ollama": check_ollama()}


@app.get("/models")
def list_models():
    import requests as _req
    try:
        r = _req.get("http://localhost:11434/api/tags", timeout=5)
        r.raise_for_status()
        models = [m["name"] for m in r.json().get("models", [])]
    except Exception:
        models = [OLLAMA_MODEL]
    return {"models": models, "default": OLLAMA_MODEL}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    start = time.time()
    try:
        result = rag_query(req.message, model=req.model or OLLAMA_MODEL)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))

    response_ms = int((time.time() - start) * 1000)

    if req.session_id:
        log_chat(
            user_message=req.message,
            answer=result["answer"],
            sources=result["sources"],
            response_ms=response_ms,
            session_id=req.session_id,
        )
        upsert_session(req.session_id, req.message)

    return {**result, "response_ms": response_ms}


@app.get("/info")
def system_info():
    from app.rag import _collection
    total_chunks = _collection.count()
    try:
        uploaded = _collection.get(where={"uploaded_by_user": {"$eq": True}})
        files: dict[str, int] = {}
        for meta in uploaded["metadatas"]:
            fname = meta.get("file_name", "unknown")
            files[fname] = files.get(fname, 0) + 1
        uploaded_docs = [{"file_name": k, "chunk_count": v} for k, v in files.items()]
    except Exception:
        uploaded_docs = []
    return {
        "ollama_model": OLLAMA_MODEL,
        "embedding_model": EMBEDDING_MODEL,
        "total_chunks": total_chunks,
        "uploaded_documents": uploaded_docs,
    }


@app.get("/source/{filename}")
def serve_source(filename: str):
    safe = Path(filename).name  # strip any path traversal
    for directory in [Path(RAW_DIR), Path(UPLOAD_DIR)]:
        matches = list(directory.rglob(safe))
        if matches:
            return FileResponse(str(matches[0]))
    raise HTTPException(status_code=404, detail=f"Source file '{safe}' not found.")


@app.get("/sessions", response_model=list[SessionSummary])
def list_sessions():
    return get_sessions()


@app.get("/sessions/{session_id}/messages", response_model=list[SessionMessage])
def session_messages(session_id: str):
    return get_session_messages(session_id)


@app.delete("/sessions/{session_id}", status_code=204)
def remove_session(session_id: str):
    delete_session(session_id)


@app.post("/upload", response_model=UploadResponse)
def upload_file(file: UploadFile = File(...)):
    ext = Path(file.filename).suffix.lower()
    if file.content_type not in ALLOWED_UPLOAD_TYPES or ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=415,
            detail="Unsupported file. Upload a PDF, HTML, or DOCX file.",
        )

    content = file.file.read(MAX_UPLOAD_BYTES + 1)
    if len(content) > MAX_UPLOAD_BYTES:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Maximum allowed size is {MAX_UPLOAD_BYTES // (1024 * 1024)} MB.",
        )

    safe_name = re.sub(r"[^A-Za-z0-9._-]", "_", Path(file.filename).name)
    sha256 = hashlib.sha256(content).hexdigest()

    from app.rag import _collection  # singleton already loaded

    if ingest.is_already_indexed(sha256):
        return UploadResponse(
            status="already_indexed",
            file_name=safe_name,
            sha256=sha256,
            chunk_count=0,
            collection_size=_collection.count(),
        )

    upload_dir = Path(UPLOAD_DIR)
    upload_dir.mkdir(parents=True, exist_ok=True)
    dest = upload_dir / f"{sha256[:12]}_{safe_name}"
    dest.write_bytes(content)

    try:
        report = ingest.ingest_file(dest)
    except Exception as e:
        dest.unlink(missing_ok=True)
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {e}")

    log_upload(
        file_name=safe_name,
        sha256=sha256,
        size_bytes=len(content),
        chunk_count=report.chunk_count,
        status="indexed",
    )

    return UploadResponse(
        status="indexed",
        file_name=safe_name,
        sha256=sha256,
        chunk_count=report.chunk_count,
        collection_size=report.collection_size,
    )
