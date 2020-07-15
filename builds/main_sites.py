
from config import CONFIG
from core.engine import Engine
from core.sites.hackernews import HackerNews
from core.sites.newsorg import Newsorg


def newsorg():
    results = []
    nws = Newsorg(CONFIG)
    for i in CONFIG.DATA:
        args = nws.create_args(query=i)
        results += nws.query(CONFIG.TOP_HEADLINE, args).articles


def hackernews():
    hk = HackerNews(CONFIG)
    hk.query()


def engine():
    ie = Engine()
    ie.execute()


def main():
    # newsorg()
    # hackernews()
    engine()


main()
