import os
import requests
import json

API_KEY = os.getenv("YOUTH_CENTER_API_KEY")
if not API_KEY:
    raise RuntimeError("YOUTH_CENTER_API_KEY not set")

BASE_URL = "https://www.youthcenter.go.kr/openapi/youthCenterList.do"

params = {
    "serviceKey": API_KEY,
    "pageIndex": 1,
    "pageSize": 10,
}

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; API-Test/1.0)",
    "Accept": "application/json",
}

res = requests.get(
    BASE_URL,
    params=params,
    headers=headers,
    timeout=30,
    allow_redirects=False,  # 핵심
)

print("STATUS:", res.status_code)
print("URL:", res.url)
print("REDIRECT:", res.headers.get("Location"))

# 🔴 JSON이 아닐 경우 처리
content_type = res.headers.get("Content-Type", "")

if "application/json" not in content_type:
    print("⚠️ JSON 응답 아님. 서버가 302 Redirect/차단 응답 반환")
    print("⚠️ 데모용 고정 JSON을 사용하거나 브라우저 기반 수집 필요")
    exit(0)

data = res.json()

with open("raw_data/youth_center_sample.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ youth_center_sample.json 저장 완료")