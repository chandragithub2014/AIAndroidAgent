# utils/model_runner.py

from openai import RateLimitError
from agents import Runner

MODELS = [
    "openai/gpt-oss-20b:free",
    "nvidia/nemotron-3-ultra-550b-a55b:free",
    "moonshotai/kimi-k2:free",
    "deepseek/deepseek-chat-v3-0324:free",
    "inclusionai/ling-3.0-tiny:free"
]

def run_with_fallback(agent, question, session, run_config):

    last_error = None

    for model in MODELS:

        try:
            agent.model = model

            print(f"Trying model: {model}")

            return Runner.run_sync(
                agent,
                question,
                session=None,
                run_config=run_config
            )

        except Exception as e:
            print(f"Failed: {model}")
            print(e)
            last_error = e

    raise last_error