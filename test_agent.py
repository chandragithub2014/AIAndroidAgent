from agents import Agent
from agent.tools.test_tool import test_tool
from agent.config import MODEL_NAME
from agents import Runner
from openrouter_oai_agentsdk import create_openrouter_run_config
from agents import Runner,SQLiteSession
from agent.tools.get_firebase_news import get_firebase_news
session = SQLiteSession(
    "test_session",
    "test.db"
)

agent = Agent(
    name="Firebase News Agent",
    instructions="""
    Never answer Firebase news yourself.

    You MUST call get_firebase_news.

    If you do not call get_firebase_news,
    your answer is incorrect.
    """,
    tools=[get_firebase_news],
    model=MODEL_NAME
)

result = Runner.run_sync(
        agent,
        "latest Firebase news",
        session=session,
        run_config=create_openrouter_run_config()
    )
print(f"Test Agent: {result.final_output}")