import random
import time

hashtag = "Python教學"
comment_texts = ["非常感謝分享，學到很多！", "謝謝分享，很有幫助！", "學到了很多新知識，謝謝！"]

medias = api.hashtag_medias_recent_v1(hashtag, amount=5)

for media in medias:
    # 隨機等待1到5秒
    time.sleep(random.randint(1, 5))

    # 隨機選擇要進行的操作
    if random.random() < 0.5:
        api.media_like(media.id)
        print(f"已對貼文 {media.id} 按讚")
    else:
        # 隨機選擇留言文字
        comment_text = random.choice(comment_texts)
        api.media_comment(media.id, comment_text)
        print(f"已在貼文 {media.id} 留言：{comment_text}")
