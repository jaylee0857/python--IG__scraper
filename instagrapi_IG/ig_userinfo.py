from instagrapi import Client
from instagrapi.exceptions import UserNotFound
from getpass import getpass
from pathlib import Path

SESSION_FILE = Path("session.json")

cl = Client()

# 優先用 session 登入（避免每次觸發驗證）
if SESSION_FILE.exists():
    cl.load_settings(SESSION_FILE)
    try:
        cl.login(None, None)  # 用已存的 settings 嘗試恢復登入狀態
    except Exception:
        pass

# 如果還沒登入成功，才要求輸入帳密
if not cl.user_id:
    username = input("Instagram username: ").strip()
    password = getpass("Instagram password (輸入時不會顯示): ")
    if not username or not password:
        raise ValueError("username/password 不能是空的")
    cl.login(username, password)
    cl.dump_settings(SESSION_FILE)

# 用「需要登入」的 API 來驗證
try:
    me = cl.account_info()
    print(f"✅ 登入成功：{me.username} | user_id={cl.user_id}")
except Exception as e:
    print("❌ 看起來尚未完成登入或 session 無效")
    print("原因：", repr(e))

# 查別人的 username（不要加 @）
target = "learntech.tw".lstrip("@")

try:
    user = cl.user_info_by_username(target)
    print(user.dict())
except UserNotFound:
    print(f"找不到帳號：{target}（可能 username 不存在/已改名/被停用，或 IG 端點風控）")
