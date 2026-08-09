from dotenv import load_dotenv
import os
import requests
from dotenv import load_dotenv
from agent.prompt_loader import load_prompt
from agents import Agent, Runner, trace, function_tool, SQLiteSession
from agent.config import MODEL_NAME

#load_dotenv(override=True)

"""
openai_api_key = os.getenv('OPENROUTER_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")
"""

print("In Interview Agent:")
interviewAgent = Agent(name="Android Interviewer", instructions=load_prompt(
        "interview_coach.txt"
    ), 
    model=MODEL_NAME)   