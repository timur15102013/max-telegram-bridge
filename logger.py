import json
import time
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

MAX_LOG = LOG_DIR / "max_log.json"
TELEGRAM_LOG = LOG_DIR / "telegram_log.json"


def save_log(file_path: Path, direction: str, text: str, raw: dict):
    record = {
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "direction": direction,
        "text": text,
        "raw": raw
    }

    with file_path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")


def save_max_log(direction: str, text: str, raw: dict):
    save_log(MAX_LOG, direction, text, raw)


def save_telegram_log(direction: str, text: str, raw: dict):
    save_log(TELEGRAM_LOG, direction, text, raw)