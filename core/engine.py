
from config import CONFIG
from libs.database import Table, Query
from .sites.newsorg import Newsorg


class Engine:
    def __init__(self):
        self._nwo_svc = Newsorg(CONFIG)

    def _treatment_base(self):
        CONFIG.LOGGING.info('---start treatment base---')
        results = []

        def analyse(article):
            for wrd in CONFIG.SCAN_WORDS:
                if article.title is not None and article.description is not None:
                    if wrd in article.title.lower() or wrd in article.description.lower():
                        return article
                return None

        def is_known(article):
            q = Query()
            if CONFIG.DB_ARTICLES.find_first(q.title == article.title) is not None:
                return True
            return False

        for i in CONFIG.DATA:
            args = self._nwo_svc.create_args(query=i)
            results += self._nwo_svc.query(CONFIG.TOP_HEADLINE, args).articles

        results = [r for r in results if analyse(r) is not None]

        for a in results:
            if not is_known(a):
                CONFIG.DB_ARTICLES.insert_obj(a)
        CONFIG.LOGGING.info('---end treatment base---')

    def _treatment_favoris(self):
        pass

    def execute(self):
        self._treatment_base()
