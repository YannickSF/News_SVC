""" API """

from flask import *
from flask_cors import CORS
from flask_restful import *

from config import CONFIG
from nws import NewsService

_web = Flask('__name__')
_cors = CORS(_web)
nwsapi = Api(_web)


class Articles(Resource):
    @staticmethod
    def get(aid=None):
        if aid is not None:
            payload = {'article': NewsService.get_article_by_id(aid)}
        else:
            payload = {'articles': NewsService.get_articles()}
        return payload

    @staticmethod
    def put():
        return {}


class Engine(Resource):
    def __init__(self):
        self.ns = NewsService()

    def get(self):
        self.ns.start_engine()
        return {'status': '0111'}


nwsapi.add_resource(Articles, '/news/articles', '/news/articles/<string:aid>')
nwsapi.add_resource(Engine, '/news/engine')


"""if __name__ == '__main__':
    _web.run(debug=CONFIG.SERVER_DEBUG, host=CONFIG.SERVER_HOST, port=CONFIG.SERVER_PORT)"""
