"""
End-to-end tests for the ELTE Chat API.

These tests hit the REAL running server with no mocks.
All assertions are structural — never assert exact LLM output strings.

Prerequisites (see plan for full instructions):
  1. ollama serve
  2. ollama pull llama3.2:3b
  3. uvicorn app.main:app --reload
  4. python -m pytest tests/e2e/ -m e2e -v --no-cov
"""

import uuid

import pytest
import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 120  # seconds — model is warmed up by conftest, but inference still takes time on 8 GB RAM

MINIMAL_PDF = (
    b"%PDF-1.4\n"
    b"1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
    b"2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj\n"
    b"3 0 obj<</Type/Page/MediaBox[0 0 612 792]/Parent 2 0 R"
    b"/Contents 4 0 R/Resources<</Font<</F1 5 0 R>>>>>>endobj\n"
    b"4 0 obj<</Length 44>>stream\n"
    b"BT /F1 12 Tf 100 700 Td (ELTE courses) Tj ET\n"
    b"endstream endobj\n"
    b"5 0 obj<</Type/Font/Subtype/Type1/BaseFont/Helvetica>>endobj\n"
    b"xref\n0 6\n0000000000 65535 f \n"
    b"0000000009 00000 n \n0000000058 00000 n \n"
    b"0000000115 00000 n \n0000000274 00000 n \n"
    b"0000000369 00000 n \n"
    b"trailer<</Size 6/Root 1 0 R>>\nstartxref\n459\n%%EOF\n"
)


# ---------------------------------------------------------------------------
# /health
# ---------------------------------------------------------------------------

@pytest.mark.e2e
def test_health_server_up():
    r = requests.get(f"{BASE_URL}/health", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "ok"
    assert "ollama" in data


@pytest.mark.e2e
def test_health_ollama_online():
    r = requests.get(f"{BASE_URL}/health", timeout=10)
    assert r.json()["ollama"] is True


# ---------------------------------------------------------------------------
# /chat
# ---------------------------------------------------------------------------

@pytest.mark.e2e
def test_chat_basic_response():
    r = requests.post(
        f"{BASE_URL}/chat",
        json={"message": "Hello"},
        timeout=TIMEOUT,
    )
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data["answer"], str)
    assert len(data["answer"]) > 0
    assert isinstance(data["sources"], list)
    assert isinstance(data["response_ms"], int)
    assert data["response_ms"] > 0


@pytest.mark.e2e
def test_chat_in_scope_question():
    r = requests.post(
        f"{BASE_URL}/chat",
        json={"message": "What is ELTE?"},
        timeout=TIMEOUT,
    )
    assert r.status_code == 200
    assert len(r.json()["answer"]) > 20


@pytest.mark.e2e
def test_chat_out_of_scope_question():
    r = requests.post(
        f"{BASE_URL}/chat",
        json={"message": "What is the capital of France?"},
        timeout=TIMEOUT,
    )
    assert r.status_code == 200
    assert len(r.json()["answer"]) > 0


@pytest.mark.e2e
def test_chat_sources_have_required_keys():
    r = requests.post(
        f"{BASE_URL}/chat",
        json={"message": "What courses are available?"},
        timeout=TIMEOUT,
    )
    assert r.status_code == 200
    for source in r.json()["sources"]:
        assert "chunk_id" in source
        assert "file" in source


@pytest.mark.e2e
def test_chat_with_session_id():
    session_id = str(uuid.uuid4())
    r = requests.post(
        f"{BASE_URL}/chat",
        json={"message": "Tell me about ELTE programs", "session_id": session_id},
        timeout=TIMEOUT,
    )
    assert r.status_code == 200

    sessions = requests.get(f"{BASE_URL}/sessions", timeout=10).json()
    assert any(s["session_id"] == session_id for s in sessions)

    # cleanup
    requests.delete(f"{BASE_URL}/sessions/{session_id}", timeout=10)


# ---------------------------------------------------------------------------
# /sessions
# ---------------------------------------------------------------------------

@pytest.mark.e2e
def test_session_created_after_chat():
    session_id = str(uuid.uuid4())
    requests.post(
        f"{BASE_URL}/chat",
        json={"message": "Session test message", "session_id": session_id},
        timeout=TIMEOUT,
    )
    sessions = requests.get(f"{BASE_URL}/sessions", timeout=10).json()
    assert any(s["session_id"] == session_id for s in sessions)

    requests.delete(f"{BASE_URL}/sessions/{session_id}", timeout=10)


@pytest.mark.e2e
def test_session_messages_retrievable():
    session_id = str(uuid.uuid4())
    requests.post(
        f"{BASE_URL}/chat",
        json={"message": "What are prerequisites?", "session_id": session_id},
        timeout=TIMEOUT,
    )
    r = requests.get(f"{BASE_URL}/sessions/{session_id}/messages", timeout=10)
    assert r.status_code == 200
    messages = r.json()
    assert len(messages) == 1
    assert messages[0]["user_message"] == "What are prerequisites?"
    assert isinstance(messages[0]["answer"], str)

    requests.delete(f"{BASE_URL}/sessions/{session_id}", timeout=10)


@pytest.mark.e2e
def test_session_delete():
    session_id = str(uuid.uuid4())
    requests.post(
        f"{BASE_URL}/chat",
        json={"message": "To be deleted", "session_id": session_id},
        timeout=TIMEOUT,
    )

    r = requests.delete(f"{BASE_URL}/sessions/{session_id}", timeout=10)
    assert r.status_code == 204

    sessions = requests.get(f"{BASE_URL}/sessions", timeout=10).json()
    assert all(s["session_id"] != session_id for s in sessions)


# ---------------------------------------------------------------------------
# /upload
# ---------------------------------------------------------------------------

@pytest.mark.e2e
def test_upload_pdf_indexed():
    r = requests.post(
        f"{BASE_URL}/upload",
        files={"file": ("e2e_test.pdf", MINIMAL_PDF, "application/pdf")},
        timeout=TIMEOUT,
    )
    assert r.status_code == 200
    data = r.json()
    assert data["status"] in ("indexed", "already_indexed")
    assert isinstance(data["chunk_count"], int)
    assert data["chunk_count"] >= 0


@pytest.mark.e2e
def test_upload_duplicate_returns_already_indexed():
    # Upload twice — second must return already_indexed
    requests.post(
        f"{BASE_URL}/upload",
        files={"file": ("dup_test.pdf", MINIMAL_PDF, "application/pdf")},
        timeout=TIMEOUT,
    )
    r = requests.post(
        f"{BASE_URL}/upload",
        files={"file": ("dup_test.pdf", MINIMAL_PDF, "application/pdf")},
        timeout=TIMEOUT,
    )
    assert r.status_code == 200
    assert r.json()["status"] == "already_indexed"


@pytest.mark.e2e
def test_upload_invalid_extension_rejected():
    r = requests.post(
        f"{BASE_URL}/upload",
        files={"file": ("notes.txt", b"plain text content", "text/plain")},
        timeout=10,
    )
    assert r.status_code == 415


# ---------------------------------------------------------------------------
# /info
# ---------------------------------------------------------------------------

@pytest.mark.e2e
def test_info_collection_size():
    r = requests.get(f"{BASE_URL}/info", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert "total_chunks" in data
    assert isinstance(data["total_chunks"], int)
    assert data["total_chunks"] >= 0


@pytest.mark.e2e
def test_info_embedding_model():
    r = requests.get(f"{BASE_URL}/info", timeout=10)
    assert r.json()["embedding_model"] == "all-MiniLM-L6-v2"


# ---------------------------------------------------------------------------
# /models
# ---------------------------------------------------------------------------

@pytest.mark.e2e
def test_models_lists_available():
    r = requests.get(f"{BASE_URL}/models", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data["models"], list)
    assert len(data["models"]) > 0
    assert "default" in data
