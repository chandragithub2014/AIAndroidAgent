from fastapi import FastAPI
from pydantic import BaseModel

from agent.android_agent import agent as android_agent
from agent.interview_agent import interviewAgent
from agents import Runner,SQLiteSession

from openrouter_oai_agentsdk import create_openrouter_run_config
from utils.model_runner import run_with_fallback

app = FastAPI()

session = SQLiteSession(
    "android_robo_session",
    "android_robo.db"
)

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str


@app.post("/chat")
def chat(request: ChatRequest):
   
    question = request.question

    if any(word in question.lower() for word in [
        "interview",
        "mock interview",
        "interview question"
    ]):
        selected_agent = interviewAgent
    else:
        selected_agent = android_agent

    result = run_with_fallback(
        selected_agent,
        question,
        session,
        create_openrouter_run_config()
     ) 

    return ChatResponse(
        answer=result.final_output
    )