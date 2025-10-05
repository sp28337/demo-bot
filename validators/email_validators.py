from pprint import pprint

from aiogram import types


def valid_email(text: str) -> bool:
    if "@" not in text or "." not in text:
        pprint(text)
        raise ValueError("Invalid email")
    return text.lower()


def valid_email_filter(message: types.Message) -> dict[str, str] | None:
    try:
        email = valid_email(message.text)
    except ValueError:
        return None

    return {"email": email}
