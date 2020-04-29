
from config import CONFIG, Query
# from libs.tools import Singleton
from core.engine import Engine


class NewsService:
    def __init__(self):
        self.engine = Engine()

    @staticmethod
    def get_articles(pagination=0):
        data = CONFIG.DB_ARTICLES.all()
        if pagination != 0:
            data = [data[i] for i in range(pagination)]
        data.reverse()
        return data

    @staticmethod
    def get_article_by_id(uid):
        q = Query()
        return CONFIG.DB_ARTICLES.find_first(q.id == uid)

    def start_engine(self):
        self.engine.execute()
