from dotenv import load_dotenv
import os
import requests
from dotenv import load_dotenv
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner, trace, function_tool, SQLiteSession
from agent.prompt_loader import load_prompt
from agent.tools.get_android_news import get_android_news
from agent.tools.get_firebase_news import get_firebase_news
from agent.tools.get_kotlin_news import get_kotlin_news
from agent.tools.search_android_docs import search_android_docs
from agent.tools.search_firebase_docs import search_firebase_docs
from agent.tools.get_compose_news import get_compose_news
from agent.config import MODEL_NAME

#load_dotenv(override=True)

"""
openai_api_key = os.getenv('OPENROUTER_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")
"""
print("In Android Agent:")
agent = Agent(name="Android Agent", instructions=load_prompt(
        "android_robo.txt"
    ), 
    tools=[
        get_android_news,get_firebase_news,get_kotlin_news,search_android_docs,get_compose_news
    ],
    model=MODEL_NAME)

print("Android Agent Tools:")
for tool in [
    get_android_news,
    get_firebase_news,
    get_kotlin_news,
    search_android_docs,
    get_compose_news,
]:
    print(tool.name)