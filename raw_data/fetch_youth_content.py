# raw_data/fetch_youth_content.py
import os
import requests
import json

API_KEY = os.getenv("YOUTH_CONTENT_API_KEY")
BASE_URL = "https://www.youthcenter.go.kr/openapi/content"

if not API_KEY:
    raise RuntimeError("YOUTH_CONTENT_API_KEY not set")

params = {
    "apiKey": API_KEY,
    "pageIndex": 1,
    "pageSize": 10,
}

res = requests.get(BASE_URL, params=params, timeout=30)
res.raise_for_status()

data = res.json()

with open("raw_data/youth_content_sample.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ youth_content_sample.json 저장 완료")