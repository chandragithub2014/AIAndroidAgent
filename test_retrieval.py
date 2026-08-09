from agent.rag.retriever import retrieve

result = retrieve(
    "What are WorkManager constraints?"
)

print(result)