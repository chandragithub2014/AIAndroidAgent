# agent/crawler/download_android_docs.py

from pathlib import Path

from agent.docs.crawler.android_urls import ANDROID_DOCS
from agent.docs.crawler.android_crawler import download_page


def download_all_docs():
    docs_dir = Path("agent/docs/android")
    docs_dir.mkdir(parents=True, exist_ok=True)

    for doc in ANDROID_DOCS:

        print(f"Downloading: {doc['name']}")

        content = download_page(doc["url"])

        file_name = f"{doc['name'].lower()}.md"

        file_content = f"""
Name: {doc['name']}
Category: {doc['category']}
Source: {doc['url']}

{content}
"""

        file_path = docs_dir / file_name

        file_path.write_text(
            file_content,
            encoding="utf-8"
        )

        print(f"Saved: {file_path}")


if __name__ == "__main__":
    download_all_docs()