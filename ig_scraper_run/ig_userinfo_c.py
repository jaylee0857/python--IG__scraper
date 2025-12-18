
import os

from instagrapi import Client
import getpass
# 建立 instagrapi 的 Client 物件
api = Client()


# 登入Instagram帳號
username = getpass.getpass()
password = getpass.getpass()
api.login(username, password)

# 取得自己的個人資料
user_info = api.user_info_by_username('learntech.tw')
print(user_info)

# # 建立儲存照片的資料夾
# if not os.path.exists("my_photos"):
#     os.mkdir("my_photos")

# # 取得自己的貼文
# my_posts = api.feed_timeline(me.pk)

# # 下載自己的貼文照片
# for post in my_posts:
#     filename = f"my_photos/{post.pk}.jpg"
#     if not os.path.exists(filename):
#         api.photo_download(post.photo_url, filename)
