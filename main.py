from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

SYSTEM_PROMPT = "You are an AI tutor that teaches machine learning and AI concepts clearly and simply. Use analogies and examples where possible."

sessions = {}

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.get("/")
def root():
    return {"status": "Gemini Web Chatbot API is running"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    if request.session_id not in sessions:
        sessions[request.session_id] = []

    history = sessions[request.session_id]

    history.append(
        types.Content(role="user", parts=[types.Part(text=request.message)])
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Content(role="user", parts=[types.Part(text=SYSTEM_PROMPT)]),
            *history
        ]
    )

    reply = response.text

    history.append(
        types.Content(role="model", parts=[types.Part(text=reply)])
    )

    sessions[request.session_id] = history

    return ChatResponse(reply=reply)

@app.delete("/session/{session_id}")
def clear_session(session_id: str):
    if session_id in sessions:
        del sessions[session_id]
    return {"status": "session cleared"}