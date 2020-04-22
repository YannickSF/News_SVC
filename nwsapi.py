""" API """

from flask import *
from flask_cors import CORS
from flask_restful import *

from config import CONFIG
from nws import NewsService


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


class NewsApi:
    def __init__(self):
        self._web = Flask('__name__')
        self._cors = CORS(self._web)
        self._ws = Api(self._web)

        self._ws.add_resource(Articles, '/articles', '/articles/<string:aid>')
        self._ws.add_resource(Engine, '/engine')

    def run(self):
        self._web.run(debug=CONFIG.SERVER_DEBUG, host=CONFIG.SERVER_HOST, port=CONFIG.SERVER_PORT)


if __name__ == '__main__':
    nsapi = NewsApi()
    nsapi.run()
