from openai import OpenAI
from dotenv import load_dotenv
from agent.crawler.android_urls import ANDROID_DOCS
from agent.crawler.firebase_urls import FIREBASE_DOCS
from agent.crawler.web_crawler import download_page
from agent.rag.chunker import chunk_text

from agent.rag.vectordb import (
    android_collection,
    firebase_collection
)

from agent.config import sync_client




def ingest_docs(docs, collection):

    for doc in docs:

        print(f"Processing {doc['name']}")

        content = download_page(
            doc["url"]
        )

        chunks = chunk_text(content)

        for idx, chunk in enumerate(chunks):

            embedding = sync_client.embeddings.create(
                model="openai/text-embedding-3-small",
                input=chunk
            )

            collection.add(
                ids=[f"{doc['name']}_{idx}"],
                documents=[chunk],
                embeddings=[embedding.data[0].embedding],
                metadatas=[{
                    "name": doc["name"],
                    "category": doc["category"],
                    "source": doc["url"]
                }]
            )


ingest_docs(
    ANDROID_DOCS,
    android_collection
)

ingest_docs(
    FIREBASE_DOCS,
    firebase_collection
)

print("Ingestion completed")