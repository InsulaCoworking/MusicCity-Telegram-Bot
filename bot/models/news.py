
from bot.bot_config import URL_BASE
from datetime import datetime
import json

from bot.utils.utils import cleanhtml

DATETIME_FORMAT_API = "%Y-%m-%dT%H:%M:%S"


class News:

    def __init__(self, id, title, excerpt, publication_date, url_path, live):
        self.id = id
        self.title = title
        self.excerpt = cleanhtml(excerpt)
        self.publication_date = publication_date
        self.url_path = url_path
        self.live = live

    def get_web_link(self):
        return f'{URL_BASE}{self.url_path}'

    def get_publication_date_human(self):
        pub_date = datetime.strptime(self.publication_date, DATETIME_FORMAT_API)
        return pub_date.strftime("%d/%m/%Y %H:%M")

    def date_url(self):
        pub_date = datetime.strptime(self.publication_date, DATETIME_FORMAT_API)
        return pub_date.strftime("%Y/%m/%d")

    @staticmethod
    def parse(news_json):
        list_news_api = json.loads(news_json)['entries']
        news_list = []
        for news_api in list_news_api:
            news = News(
                news_api['id'],
                news_api['title'],
                news_api['excerpt'],
                news_api['date'],
                news_api['url_path'],
                news_api['live'],
            )

            if news.live and news.url_path.startswith('/blog/'):
                news_list.append(news)

        news_sorted = sorted(
            news_list,
            key=lambda x: datetime.strptime(x.publication_date, DATETIME_FORMAT_API), reverse=False
        )

        return news_sorted


