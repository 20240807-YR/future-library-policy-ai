# raw_data/fetch_youth_policy.py
import os
import requests
import json

API_KEY = os.getenv("YOUTH_POLICY_API_KEY")
BASE_URL = "https://www.youthcenter.go.kr/openapi/policy"

if not API_KEY:
    raise RuntimeError("YOUTH_POLICY_API_KEY not set")

params = {
    "apiKey": API_KEY,
    "pageIndex": 1,
    "pageSize": 10,
    "srchWord": "주거",
}

res = requests.get(BASE_URL, params=params, timeout=30)
res.raise_for_status()

data = res.json()

with open("raw_data/youth_policy_sample.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ youth_policy_sample.json 저장 완료")