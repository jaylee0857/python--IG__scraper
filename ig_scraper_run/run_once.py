# -*- coding: utf-8 -*-
#%%
from instagram_posts_scraper.instagram_posts_scraper import InstaPeriodScraper


target_info = {"username": "web_885", "days_limit":14}
ig_posts_scraper = InstaPeriodScraper()
res = ig_posts_scraper.get_posts(target_info=target_info)
# res
print(res)
# %%

# ts2991raby