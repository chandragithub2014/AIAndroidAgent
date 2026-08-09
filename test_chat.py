
# test_chat.py

from agent.config import async_client
import asyncio

async def main():
    response = await async_client.responses.create(
        model="meta-llama/llama-3.1-8b-instruct",
        input="Say hello"
    )

    print(response.output_text)

asyncio.run(main())