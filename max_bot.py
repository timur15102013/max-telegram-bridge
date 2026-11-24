import aiohttp

from config import MAX_API_URL, MAX_TOKEN, MAX_CHAT_ID
from logger import save_max_log


async def send_message(text: str):
    url = f"{MAX_API_URL}/messages"
    headers = {
        "Authorization": MAX_TOKEN,
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        response = await session.post(url, headers=headers, json={
            "chat_id": MAX_CHAT_ID,
            "text": f"[Из Telegram] {text}"
        })

    save_max_log(
        "sent_from_telegram",
        text,
        {"http_status": response.status}
    )

    return response.status


def get_text(update: dict):
    message = update.get("message", {})
    body = message.get("body", {})
    return body.get("text")


def get_chat_id(update: dict):
    return update.get("chat_id")