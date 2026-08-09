from pathlib import Path

def load_prompt(file_name: str) -> str:
    return Path(
        f"prompts/{file_name}"
    ).read_text(encoding="utf-8")