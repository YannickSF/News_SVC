
from nws import NewsService


class FeedCreator:

    @staticmethod
    def articles_to_items():
        arts = NewsService.get_articles()
        return arts

    def json_feed(self):
        return {"version": "https://jsonfeed.org/version/1",
                "title": "News.YSF Feed",
                "home_page_url": "https://news.yannicksf.com/",
                "feed_url": "https://news.sylys.space/feed",
                "items": self.articles_to_items()}
