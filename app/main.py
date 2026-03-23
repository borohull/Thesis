from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.rag import rag_query, check_ollama

app = FastAPI(title="ELTE IK Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[dict]


@app.get("/health")
def health():
    return {"status": "ok", "ollama": check_ollama()}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        result = rag_query(req.message)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    return result
