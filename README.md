# ig_scraper_run（一次跑過看到結果）

目標：在 Windows 上只跑一次 `run_once.py`，看到輸出 `result.json` 就結束。

---

python --version

python -m pip install --upgrade pip
python -m pip install instagram-posts-scraper requests beautifulsoup4 cloudscraper pandas pytz seleniumbase lxml




target_info = {"username": "kaicenat", "days_limit": 5}  # 改成你要測的帳號
scraper = InstaPeriodScraper()
res = scraper.get_posts(target_info=target_info)

# updated_at 是 datetime，轉成字串避免 json dump 失敗
if "updated_at" in res:
    res["updated_at"] = str(res["updated_at"])

print(json.dumps(res, ensure_ascii=False, indent=2))

with open("result.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=2)

print("Saved -> result.json")


執行 python run_once.py
