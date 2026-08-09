from agent.config import sync_client

result = sync_client.embeddings.create(
    model="openai/text-embedding-3-small",
    input="What is WorkManager?"
)

print(
    f"Embedding length = "
    f"{len(result.data[0].embedding)}"
)