# rag/ingest.py

from pathlib import Path
from openai import OpenAI

from agent.rag.chunker import chunk_text
from agent.rag.vectordb import collection

from dotenv import load_dotenv
import os

from agent.config import sync_client

#docs_path = Path("agent/docs/android")
docs_path = Path("agent/docs/android")

for file in docs_path.glob("*.md"):

    content = file.read_text(encoding="utf-8")

    chunks = chunk_text(content)

    for idx, chunk in enumerate(chunks):

        embedding = sync_client.embeddings.create(
            model="openai/text-embedding-3-small",
            input=chunk
        )

        collection.add(
            ids=[f"{file.stem}_{idx}"],
            documents=[chunk],
            embeddings=[embedding.data[0].embedding],
            metadatas=[{
                "source": file.name
            }]
        )

print("Ingestion completed")