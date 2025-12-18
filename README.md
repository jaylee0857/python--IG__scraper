# ig_scraper_run（One-time Runner）

目標：在 Windows 上「只跑一次」抓取指定 IG 帳號資料，並輸出 `result.json`。

> 這個資料夾是 **Runner**（執行用）。原始碼（src）請放另一個資料夾，避免混在一起。

---

確認 Python 已安裝
在 PowerShell 執行：
python --version
---
##安裝必要套件
python -m pip install --upgrade pip
python -m pip install instagram-posts-scraper requests beautifulsoup4 cloudscraper pandas pytz seleniumbase lxml
---

##建立 run_once.py
```
# -*- coding: utf-8 -*-
from instagram_posts_scraper.instagram_posts_scraper import InstaPeriodScraper
import json

# 改成你要測的帳號
target_info = {"username": "kaicenat", "days_limit": 5}

scraper = InstaPeriodScraper()
res = scraper.get_posts(target_info=target_info)

# updated_at 是 datetime，轉成字串避免 json.dump 失敗
if "updated_at" in res:
    res["updated_at"] = str(res["updated_at"])

print(json.dumps(res, ensure_ascii=False, indent=2))

with open("result.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=2)

print("Saved -> result.json")
```

---
#執行
python run_to_json.py
---
輸出json