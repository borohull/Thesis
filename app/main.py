from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    message: str


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"


@app.post("/chat")
def chat(req: ChatRequest):

    payload = {
        "model": MODEL,
        "prompt": req.message,
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload)
    response = r.json()["response"]

    return {"answer": response}