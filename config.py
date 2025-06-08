import os
import json
from dotenv import load_dotenv

load_dotenv()


def get_settings():
    # .env優先、なければsettings.json
    url = os.getenv("REDMINE_URL")
    api_key = os.getenv("REDMINE_API_KEY")
    if url and api_key:
        return {"redmine_url": url, "redmine_api_key": api_key}
    # settings.json
    if os.path.exists("settings.json"):
        with open("settings.json", encoding="utf-8") as f:
            return json.load(f)
    raise RuntimeError("設定ファイル(.envまたはsettings.json)が見つかりません")
