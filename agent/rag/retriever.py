# rag/retriever.py

# rag/retriever.py

from openai import OpenAI
from agent.rag.vectordb import android_collection
from agent.rag.vectordb import firebase_collection

from dotenv import load_dotenv
import os
from agent.config import sync_client



def retrieve(query: str, collection) -> str:

    embedding = sync_client.embeddings.create(
        model="openai/text-embedding-3-small",
        input=query
    )

    results = collection.query(
        query_embeddings=[
            embedding.data[0].embedding
        ],
        n_results=3
    )

    docs = results["documents"][0]

    return "\n\n".join(docs)

def retrieve_without_collections(query: str) -> str:

    embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )

    results = collection.query(
        query_embeddings=[
            embedding.data[0].embedding
        ],
        n_results=3
    )

    docs = results["documents"][0]

    return "\n\n".join(docs)

def retrieve_old(query: str, chunks: list[dict]) -> str:

    query_words = query.lower().split()

    best_chunk = None
    best_score = 0

    for chunk in chunks:

        score = 0

        chunk_text = chunk["text"].lower()

        for word in query_words:
            if word in chunk_text:
                score += 1

        if score > best_score:
            best_score = score
            best_chunk = chunk

    if not best_chunk:
        return "No relevant Android documentation found."

    return (
        f"Source: {best_chunk['source']}\n\n"
        f"{best_chunk['text']}"
    )


def retrieve_original(query: str, chunks: list[str]) -> str:

    query_words = query.lower().split()

    best_chunk = ""
    best_score = 0

    for chunk in chunks:

        score = 0

        chunk_lower = chunk.lower()

        for word in query_words:
            if word in chunk_lower:
                score += 1

        if score > best_score:
            best_score = score
            best_chunk = chunk

    return best_chunk