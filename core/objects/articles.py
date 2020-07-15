
import uuid


class Article:
    def __init__(self, args):
        self.id = str(uuid.uuid4())

        if 'author' or 'by' in args.keys():
            if 'by' in args.keys():
                self.author = args['by']
            else:
                self.author = args['author']
        else:
            self.author = None

        if 'title' in args.keys():
            self.title = args['title']
        else:
            self.author = None

        if 'description' in args.keys():
            self.description = args['description']
        else:
            self.description = None

        if 'url' in args.keys():
            self.url = args['url']
        else:
            self.url = None

        if 'source' in args.keys():
            self.source = args['source']
        else:
            self.source = None

        if 'urlToImage' in args.keys():
            self.urlToImage = args['urlToImage']
        else:
            self.urlToImage = None

        if 'publishedAt' in args.keys():
            self.publishedAt = args['publishedAt']
        else:
            self.publishedAt = None

        if 'content' in args.keys():
            self.content = args['content']
        else:
            self.content = None

        if 'favoris' in args.keys():
            self.favoris = args['favoris']
        else:
            self.favoris = None

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
