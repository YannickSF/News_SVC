
# import datetime
# import logging
from libs.database import Table, Query


class _Config:
    # SERVER CONFIG
    SEVER_SECRET_KEY = 'secret_key_for_test'
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 5000
    SERVER_DEBUG = True
    """
    # LOG
    date = datetime.datetime.now()
    date = date.strftime("%d%m%Y")
    logging.basicConfig(filename='datas/news_{0}.log'.format(date), level=logging.INFO)
    LOGGING = logging"""

    # NewsOrg - configuration
    NEWS_API_KEY = ''

    NEWS_ORG = 'https://newsapi.org/v2/'
    EVERYTHING = 'everything'
    HEADLINE = 'headline'
    TOP_HEADLINE = 'top-headlines'

    DATA = [{'country': 'fr', 'category': 'business'},
            {'country': 'fr', 'category': 'science'},
            {'country': 'fr', 'category': 'technology'},
            {'sources': 'techradar'}, {'sources': 'techcrunch'}, {'sources': 'recode'}]

    SCAN_WORDS = ['ai', 'ia', 'space', 'business']

    # DATABASE
    DB_ARTICLES = Table('articles')


CONFIG = _Config()
