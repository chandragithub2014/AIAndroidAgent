from agents import Agent

from agent.android_agent import agent as android_agent
from agent.interview_agent import interviewAgent

from agent.config import MODEL_NAME

#print("Android Agent:", android_agent.name)
#print("Interview Agent:", interviewAgent.name)
#print("Model:", MODEL_NAME)
router_agent = Agent(
    name="Router Agent",
    instructions="""
You are ONLY a dispatcher.

You have NO tools.

For Android questions, ALWAYS transfer to Android Agent.
For interview questions, ALWAYS transfer to Interview Agent.

Never answer.
Never call tools.
Never perform work yourself.
Only transfer.
""",
    handoffs=[
        android_agent,
        interviewAgent
    ],
    model=MODEL_NAME
)
print("Android Agent:", android_agent.name)
print("Interview Agent:", interviewAgent.name)
print("Handoffs:", len([
    android_agent,
    interviewAgent
]))