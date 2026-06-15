import json
from pathlib import Path

from app.schemas import ContactMessage


FILE_PATH = Path(__file__).resolve().parents[1] / "data" / "contact.json"


def save_contact(contact: ContactMessage) -> dict:
    messages = []

    if FILE_PATH.exists():
        with FILE_PATH.open("r", encoding="utf-8") as file:
            messages = json.load(file)

    saved_contact = contact.model_dump(mode="json")
    messages.append(saved_contact)

    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with FILE_PATH.open("w", encoding="utf-8") as file:
        json.dump(messages, file, indent=4, ensure_ascii=False)

    return saved_contact
