import requests
import chromadb
from sentence_transformers import SentenceTransformer
from app.settings import (
    CHROMA_PATH, COLLECTION_NAME, EMBEDDING_MODEL, TOP_K,
    OLLAMA_URL, OLLAMA_MODEL, TEMPERATURE, TIMEOUT_S,
)

# Singletons — loaded once on import, not per request
_client     = chromadb.PersistentClient(path=CHROMA_PATH)
_collection = _client.get_collection(name=COLLECTION_NAME)
_model      = SentenceTransformer(EMBEDDING_MODEL)


def retrieve(query: str, n_results: int = TOP_K) -> list[dict]:
    query_emb = _model.encode([query]).tolist()
    results   = _collection.query(query_embeddings=query_emb, n_results=n_results)
    return [
        {"content": doc, "metadata": meta}
        for doc, meta in zip(results["documents"][0], results["metadatas"][0])
    ]


def build_prompt(query: str, chunks: list[dict]) -> str:
    context = "\n\n".join(
        f"[Source: {c['metadata']['file_name']}]\n{c['content']}"
        for c in chunks
    )
    return f"""You are a helpful assistant for ELTE Faculty of Informatics students. Answer the question using only the context below. If the answer is not in the context, say so.

Context:
{context}

Question: {query}
Answer:"""


def check_ollama() -> bool:
    try:
        # Derive base URL from OLLAMA_URL (strip the /api/generate path)
        base = OLLAMA_URL.split("/api/")[0]
        r = requests.get(base, timeout=5)
        return r.status_code == 200
    except requests.exceptions.ConnectionError:
        return False


def call_ollama(prompt: str, model: str = OLLAMA_MODEL) -> str:
    if not check_ollama():
        raise RuntimeError("Ollama is not running. Start it with: ollama serve")

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": TEMPERATURE, "num_ctx": 2048},
    }

    try:
        r = requests.post(OLLAMA_URL, json=payload, timeout=TIMEOUT_S)
        r.raise_for_status()
        return r.json()["response"].strip()
    except requests.exceptions.Timeout:
        raise RuntimeError(f"Ollama timed out after {TIMEOUT_S}s — model may still be loading")
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Ollama HTTP {e.response.status_code} — is model '{model}' pulled?")
    except KeyError:
        raise RuntimeError(f"Unexpected Ollama response: {r.text[:200]}")


def rag_query(query: str, model: str = OLLAMA_MODEL) -> dict:
    chunks = retrieve(query)
    prompt = build_prompt(query, chunks)
    answer = call_ollama(prompt, model=model)
    return {
        "answer": answer,
        "sources": [
            {"chunk_id": c["metadata"]["chunk_id"], "file": c["metadata"]["file_name"]}
            for c in chunks
        ],
    }
