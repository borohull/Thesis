"""
E2E conftest — session-scoped fixtures that skip all tests if the
live server or Ollama is not reachable. Applied automatically to
every test in this directory via autouse=True.
"""

import pytest
import requests

BASE_URL = "http://localhost:8000"


def _health() -> dict | None:
    try:
        r = requests.get(f"{BASE_URL}/health", timeout=5)
        if r.status_code == 200:
            return r.json()
    except requests.exceptions.ConnectionError:
        pass
    return None


@pytest.fixture(scope="session", autouse=True)
def live_server():
    """Skip the entire E2E session if the FastAPI server is not running."""
    if _health() is None:
        pytest.skip(
            "FastAPI server not running — start it with:\n"
            "  uvicorn app.main:app --reload"
        )


@pytest.fixture(scope="session", autouse=True)
def ollama_up(live_server):
    """Skip the entire E2E session if Ollama is not reachable."""
    health = _health()
    if health is None or not health.get("ollama"):
        pytest.skip(
            "Ollama not running — start it with:\n"
            "  ollama serve\n"
            "Then pull the model if not already done:\n"
            "  ollama pull llama3.2:3b"
        )


@pytest.fixture(scope="session", autouse=True)
def warm_up_model(ollama_up):
    """
    Fire one real /chat request before any tests run so the LLM is loaded
    into RAM. First inference on a cold Ollama can take 2-5 minutes on 8 GB
    RAM — without this, early tests time out while the model is still loading.
    """
    try:
        requests.post(
            f"{BASE_URL}/chat",
            json={"message": "Hello"},
            timeout=300,  # allow up to 5 min for cold model load
        )
    except Exception:
        pass  # warm-up best-effort; individual tests will surface real failures


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL
