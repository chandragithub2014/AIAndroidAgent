# main.py
import agent.config
from agent.android_agent import agent as android_agent
from agent.interview_agent import interviewAgent as interview_agent
from agents import Runner,SQLiteSession
from openrouter_oai_agentsdk import create_openrouter_run_config
#from agent.router_agent import router_agent



session = SQLiteSession(
    "android_robo_session",
    "android_robo.db"
)


while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    if any(word in user_input.lower() for word in [
        "interview",
        "mock interview",
        "interview question"
    ]):
        selected_agent = interview_agent
    else:
        selected_agent = android_agent

    try:
        result = Runner.run_sync(
            selected_agent,
            user_input,
            session=session,
            run_config=create_openrouter_run_config()
        )
        print("Final agent:", result.last_agent.name)
        print("Output:", result.final_output)
    except Exception as e:
        print("Model temporarily unavailable.")
        print(str(e))    
"""
    result = Runner.run_sync(
        router_agent,
        user_input,
        session=session,
        run_config=create_openrouter_run_config()
    )
    print("Final agent:", result.last_agent.name)
    print("Output:", result.final_output)
"""
"""
    if user_input.startswith("/interview"):
        result = Runner.run_sync(
            interview_agent,
            user_input.replace("/interview", "").strip(),
            session=session,
             run_config=create_openrouter_run_config()
        )

        print(f"Interviewer: {result.final_output}")
    else:
        result = Runner.run_sync(
            android_agent,
            user_input,
            session=session,
            run_config=create_openrouter_run_config()
        )
"""
      
    #print(f"Android Robo: {result.final_output}")

