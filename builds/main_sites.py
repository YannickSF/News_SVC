# coding: utf8

from config import CONFIG
from core.engine import Engine
from core.sites.hackernews import HackerNews
from core.sites.newsorg import Newsorg

import requests
from requests import RequestException
from xmljson import badgerfish as bf
from xml.etree.ElementTree import Element, tostring, fromstring
import feedparser
from json import dumps


def newsorg():
    results = []
    nws = Newsorg(CONFIG)
    for i in CONFIG.DATA:
        args = nws.create_args(query=i)
        results += nws.query(CONFIG.TOP_HEADLINE, args).articles


def hackernews():
    hk = HackerNews(CONFIG)
    hk.query()


def rss():
    try:
        # request site
        url = 'https://siecledigital.fr/feed'
        requete = requests.get(url)
        print(requete)
        print('-----------')
        # convert str
        print(str(requete.content, 'utf-8'))
        test = bf.data(fromstring(str(requete.content, 'utf-8')))
        # json convertion
        test_jsn = dumps(test, ensure_ascii=False)
        print('-------')
        d = dict(test_jsn[1:len(test_jsn)-2])
        print(d)
    except RequestException:
        return None


def rss_parser():
    url = 'https://siecledigital.fr/feed'
    news_feed = feedparser.parse(url)
    print(news_feed.feed.title)


def engine():
    ie = Engine()
    ie.execute()


def main():
    # newsorg()
    # hackernews()
    # engine()
    # rss()
    rss_parser()


main()
