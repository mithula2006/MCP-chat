from fastapi import FastAPI
from pydantic import BaseModel
from mcp_tools import query_policies

app = FastAPI(title="Student Policy Chat")

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
def chat(req: ChatRequest):
    answer = query_policies(req.question)
    return {
        "answer": answer
    }
