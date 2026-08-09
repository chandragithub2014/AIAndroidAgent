from pathlib import Path

def load_document(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

def load_all_documents(directory: str) -> list[tuple[str, str]]:
    docs = []

    for file in Path(directory).glob("*.md"):
        content = file.read_text(encoding="utf-8")
        docs.append((file.name, content))

    return docs    