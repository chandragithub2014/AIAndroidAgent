from agents import function_tool
from googlesearch import search
import requests
from bs4 import BeautifulSoup
from agent.docs.docloader.document_loader import load_document
from agent.rag.chunker import chunk_text
from agent.rag.retriever import retrieve
from agent.rag.vectordb import firebase_collection

@function_tool
def search_firebase_docs(query: str) -> str:
    return retrieve(query,firebase_collection)

