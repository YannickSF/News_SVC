
from .articles import Article


class Result:
    def __init__(self, args):
        if args is not None:
            if args != {}:
                self.status = args['status']
                self.totalResults = args['totalResults']
                self.articles = []

        for art in args['articles']:
            self.articles.append(Article(art))

    def __repr__(self):
        return {'status': self.status, 'totalResult': self.totalResults, 'articles': self.articles}

    def __str__(self):
        return self.__repr__().__str__()