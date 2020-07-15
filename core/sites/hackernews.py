
import requests
from requests import RequestException
from core.objects.articles import Article


class HackerNews:
    def __init__(self, config):
        self._config = config

    def create_args(self):
        pass

    def _get_topstories(self):
        try:
            url = self._config.HACKERSNEWS_API + self._config.TOP_STORIES + self._config.OPT_JSON + self._config.OPT_PRETTY
            requete = requests.get(url)
            return requete.json()
        except RequestException:
            return None

    def _get_item(self, iid):
        try:
            url = self._config.HACKERSNEWS_API + self._config.OPT_ITEMS + '/{0}'.format(str(iid)) + self._config.OPT_JSON +\
                  self._config.OPT_PRETTY
            requete = requests.get(url)
            return requete.json()
        except RequestException:
            return None

    def query(self):
        results = []
        top_stories = self._get_topstories()

        for i in top_stories:
            results.append(Article(self._get_item(i)))

        return results
