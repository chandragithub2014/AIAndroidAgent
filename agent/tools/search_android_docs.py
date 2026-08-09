from agents import function_tool
from googlesearch import search
import requests
from bs4 import BeautifulSoup
from agent.docs.docloader.document_loader import load_document
from agent.rag.chunker import chunk_text
from agent.rag.retriever import retrieve
from agent.rag.vectordb import android_collection

@function_tool
def search_android_docs(query: str) -> str:
    print("******** SEARCH ANDROID DOCS TOOL CALLED ********")
    return retrieve(query,android_collection)

@function_tool
def search_android_docs_old(query: str) -> str:
    try:
            docs = load_all_documents(
                "agent/docs/android"
            )

            all_chunks = []

            for filename, content in docs:

                chunks = chunk_text(content)

                for chunk in chunks:
                    all_chunks.append({
                        "source": filename,
                        "text": chunk
                    })

            result = retrieve(query, all_chunks)

            return result
    except Exception as e:
           return f"Tool Error: {type(e).__name__}: {e}"

@function_tool
def search_android_docs_original(query: str) -> str:
    try:
        #print("In Search android_docs")
        #print(f"Query = {query}")
        content = load_document(
            "agent/docs/android/workmanager.md"
        )
        docs = load_all_documents(
            "agent/docs/android"
        )
        #print(f"Document length = {len(content)}")
        chunks = chunk_text(content)
        #print(f"Chunks count = {len(chunks)}")
        result = retrieve(query, chunks)
        #print(f"Result = {result[:200]}")
        return result
    except Exception as e:
        #print(f"Exception Type: {type(e).__name__}")
        #print(f"Exception Message: {e}")
        return f"Tool Error: {type(e).__name__}: {e}" 