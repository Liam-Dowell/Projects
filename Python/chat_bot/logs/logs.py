import datetime
import json
from pathlib import Path

LOG_PATH = Path("/workspaces/Projects/Python/chat_bot/logs.jsonl")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

def create_logs(user_input):
    # logs accepts user input as a agruements
    # it logs the users input to a json file

    rec = {
        "ts": datetime.datetime.now().isoformat() + "Z",
        "text": user_input
    }

    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

def erase_logs():
    pass