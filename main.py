import json

from fastapi import FastAPI, Request

from config import MAX_CHAT_ID, TELEGRAM_CHAT_ID
from logger import save_max_log, save_telegram_log
from telegram_bot import send_message as send_to_telegram, get_text as get_telegram_text, get_chat_id as get_telegram_chat_id
from max_bot import send_message as send_to_max, get_text as get_max_text, get_chat_id as get_max_chat_id

app = FastAPI()


@app.get("/")
async def home():
    return {"status": "MAX <-> Telegram bridge is running"}


@app.post("/max-webhook")
async def max_webhook(request: Request):
    update = await request.json()

    print("MAX UPDATE:")
    print(json.dumps(update, ensure_ascii=False, indent=2))

    text = get_max_text(update)
    chat_id = get_max_chat_id(update)

    if text:
        save_max_log("received_from_max", text, update)

        if chat_id == MAX_CHAT_ID:
            await send_to_telegram(text)

    return {"ok": True}


@app.post("/telegram-webhook")
async def telegram_webhook(request: Request):
    update = await request.json()

    print("TELEGRAM UPDATE:")
    print(json.dumps(update, ensure_ascii=False, indent=2))

    text = get_telegram_text(update)
    chat_id = get_telegram_chat_id(update)

    if text:
        save_telegram_log("received_from_telegram", text, update)

        if chat_id == TELEGRAM_CHAT_ID:
            await send_to_max(text)

    return {"ok": True}