# -*- coding: utf-8 -*-
from instagram_posts_scraper.instagram_posts_scraper import InstaPeriodScraper
import webbrowser
import re

# IG shortcode 通常長這樣：A-Za-z0-9-_，而且不會是純數字
_SHORTCODE_RE = re.compile(r"^[A-Za-z0-9_-]{5,30}$")

def is_ig_shortcode(s: str) -> bool:
    if not s:
        return False
    if s.isdigit():
        return False
    return bool(_SHORTCODE_RE.match(s))

def to_ig_post_url_from_shortcode(sc: str) -> str | None:
    if not is_ig_shortcode(sc):
        return None
    return f"https://www.instagram.com/p/{sc}/"

target_info = {"username": "web_885", "days_limit": 14}

scraper = InstaPeriodScraper()
res = scraper.get_posts(target_info=target_info)

print(f"account_status = {res.get('account_status')}")

# 優先用 init_posts（通常這裡就是正確 shortcode）
shortcodes = res.get("init_posts", []) or []

#  如果 init_posts 沒東西，再從 data 裡找「像 shortcode 的欄位」
if not shortcodes:
    items = res.get("data", []) or []
    for it in items:
        for key in ("shortcode", "code", "short_code"):
            v = it.get(key)
            if isinstance(v, str) and is_ig_shortcode(v):
                shortcodes.append(v)
                break

# 去重 + 組 URL
seen = set()
urls = []
for sc in shortcodes:
    url = to_ig_post_url_from_shortcode(str(sc))
    if not url or url in seen:
        continue
    seen.add(url)
    urls.append(url)

print(f"posts queued   = {len(urls)}")

# 先印前 5 個網址確認
for u in urls[:5]:
    print(u)

# 逐篇開啟手動操作
for url in urls:
    webbrowser.open_new_tab(url)
    input("看完後按 Enter 開下一篇...")  # ← 這行才是正確寫法（把「改在哪」拿掉或變註解）
