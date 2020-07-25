""" API """

from flask import *
from flask_cors import CORS
from flask_restful import *

from config import CONFIG
from nws import NewsService
from libs.jsonfeed import FeedCreator


_web = Flask('__name__')
_cors = CORS(_web)
nwsapi = Api(_web)


class Health(Resource):
    @staticmethod
    def _osciloscope():
        url = 'http://localhost:5000/articles'
        care = {'1': True, '2': True}
        return care

    def get(self):
        return self._osciloscope()


class Articles(Resource):
    @staticmethod
    def get(aid=None):
        if aid is not None:
            payload = {'code': 200, 'article': NewsService.get_article_by_id(aid)}
        else:
            p = 0
            if len(request.args) > 0:
                p = int(request.args.get('p'))
            payload = {'code': 200, 'articles': NewsService.get_articles(p)}
        return payload

    @staticmethod
    def put():
        return {}


class Engine(Resource):
    def __init__(self):
        self.ns = NewsService()

    def get(self):
        self.ns.start_engine()
        return {'code': 200, 'status': '0111'}


class JSONFeed(Resource):
    def __init__(self):
        self.fder = FeedCreator()

    def get(self):
        return self.fder.json_feed()


nwsapi.add_resource(Engine, '/engine')
nwsapi.add_resource(Articles, '/articles', '/articles/<string:aid>')

nwsapi.add_resource(Health, '/health')
nwsapi.add_resource(JSONFeed, '/feed')


if __name__ == '__main__':
    _web.run(debug=CONFIG.SERVER_DEBUG, host=CONFIG.SERVER_HOST, port=CONFIG.SERVER_PORT)
