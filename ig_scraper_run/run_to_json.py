# -*- coding: utf-8 -*-
from instagram_posts_scraper.instagram_posts_scraper import InstaPeriodScraper
import json

# 改成你要測的帳號
target_info = {"username": "web_885", "days_limit": 5}

scraper = InstaPeriodScraper()
res = scraper.get_posts(target_info=target_info)

# updated_at 是 datetime，轉成字串避免 json.dump 失敗
if "updated_at" in res:
    res["updated_at"] = str(res["updated_at"])

print(json.dumps(res, ensure_ascii=False, indent=2))

with open("result.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=2)

print("Saved -> result.json")
