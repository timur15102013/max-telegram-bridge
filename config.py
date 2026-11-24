import os
from dotenv import load_dotenv

load_dotenv()

MAX_TOKEN = os.getenv("MAX_TOKEN")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

MAX_CHAT_ID = int(os.getenv("MAX_CHAT_ID", "0"))
TELEGRAM_CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID", "0"))

MAX_API_URL = "https://platform-api2.max.ru"
TELEGRAM_API_URL = "https://api.telegram.org"