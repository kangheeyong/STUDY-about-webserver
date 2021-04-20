import json
import requests

API_ID = ""
# REAT API KEY
AUTH = ""
PLAYER_ID = ""

TITLE = "제목"
BODY = "내용"
WEB_URL = "https://www.naver.com"

header = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Basic {AUTH}"
}

payload = {
    "app_id": API_ID,
    "include_player_ids": [PLAYER_ID],
    "headings": {"en": TITLE},
    "contents": {"en": BODY},
    "web_url": WEB_URL,
}

req = requests.post(
    "https://onesignal.com/api/v1/notifications",
    headers=header,
    data=json.dumps(payload),
)

print(req.status_code, req.reason, req.json())
