
from config import CONFIG
from libs.database import Table, Query
from .sites.newsorg import Newsorg
from .sites.hackernews import HackerNews


class Engine:
    def __init__(self):
        self._nwo_svc = Newsorg(CONFIG)
        self._hks_svc = HackerNews(CONFIG)

    def _treatment_base(self):
        # CONFIG.LOGGING.info('---start treatment base---')
        results_nws = []
        results_hks = []

        def analyse(article):
            for wrd in CONFIG.SCAN_WORDS:
                if article.title is not None:
                    if wrd in article.title.lower():
                        return article

                if article.description is not None:
                    if wrd in article.description.lower():
                        return article
                return None

        def is_known(article):
            q = Query()
            if CONFIG.DB_ARTICLES.find_first(q.title == article.title) is not None:
                return True
            return False

        for i in CONFIG.DATA:
            args = self._nwo_svc.create_args(query=i)
            results_nws += self._nwo_svc.query(CONFIG.TOP_HEADLINE, args).articles

        results_hks += self._hks_svc.query()

        results = [r for r in results_nws + results_hks if analyse(r) is not None]

        for a in results:
            if not is_known(a):
                CONFIG.DB_ARTICLES.insert_obj(a)
        # CONFIG.LOGGING.info('---end treatment base---')

    def _treatment_favoris(self):
        pass

    def execute(self):
        self._treatment_base()
