""" API """

from flask import *
from flask_cors import CORS
from flask_restful import *

from config import CONFIG
from nws import NewsService

_web = Flask('__name__')
_cors = CORS(_web)
nwsapi = Api(_web)


class Health(Resource):
    @staticmethod
    def get():
        return 'NEWS API UP'


class Articles(Resource):
    @staticmethod
    def get(aid=None):
        if aid is not None:
            payload = {'article': NewsService.get_article_by_id(aid)}
        else:
            p = 0
            if len(request.args) > 0:
                p = int(request.args.get('p'))
            payload = {'articles': NewsService.get_articles(p)}
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


nwsapi.add_resource(Health, '/')
nwsapi.add_resource(Articles, '/articles', '/articles/<string:aid>')
nwsapi.add_resource(Engine, '/engine')


if __name__ == '__main__':
    _web.run(debug=CONFIG.SERVER_DEBUG, host=CONFIG.SERVER_HOST, port=CONFIG.SERVER_PORT)
