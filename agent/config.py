from openai import AsyncOpenAI
from agents import set_default_openai_client
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

# Sync client (for embeddings)
api_key = os.getenv("OPEN_ROUTER_API_KEY")
#MODEL_NAME = "meta-llama/llama-3.1-8b-instruct"
#MODEL_NAME= "openai/gpt-oss-20b:free"
MODEL_NAME= "inclusionai/ling-3.0-tiny:free"
sync_client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

async_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

set_default_openai_client(async_client,
    use_for_tracing=False)