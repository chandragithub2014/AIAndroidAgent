import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

android_collection = client.get_or_create_collection(
    name="android_docs"
)

firebase_collection = client.get_or_create_collection(
    "firebase_docs"
)