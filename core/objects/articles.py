
import uuid


class Article:
    def __init__(self, args):
        if 'id' not in args.keys():
            self.id = str(uuid.uuid4())
        else:
            self.id = args['id']
        self.author = args['author']
        self.title = args['title']
        self.description = args['description']
        self.url = args['url']
        self.source = args['source']
        self.urlToImage = args['urlToImage']
        self.publishedAt = args['publishedAt']
        self.content = args['content']
        self.favoris = False

    def __repr__(self):
        return {'id': self.id,
                'author': self.author,
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'source': self.source,
                'urlToImage': self.urlToImage,
                'publishAt': self.publishedAt,
                'content': self.content,
                'favoris': self.favoris}

    def __str__(self):
        return self.__repr__().__str__()
