import aiohttp

from config import TELEGRAM_API_URL, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
from logger import save_telegram_log


async def send_message(text: str):
    url = f"{TELEGRAM_API_URL}/bot{TELEGRAM_TOKEN}/sendMessage"

    async with aiohttp.ClientSession() as session:
        response = await session.post(url, json={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": f"[Из MAX] {text}"
        })

    save_telegram_log(
        "sent_from_max",
        text,
        {"http_status": response.status}
    )

    return response.status


def get_text(update: dict):
    message = update.get("message", {})
    return message.get("text")


def get_chat_id(update: dict):
    message = update.get("message", {})
    return message.get("chat", {}).get("id")