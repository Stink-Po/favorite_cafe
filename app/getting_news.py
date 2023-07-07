import requests
import json
import os
import datetime
from app.config import Config


class NewsService:
    def __init__(self):
        self.today = datetime.date.today()
        self.filename = os.path.join(Config.NEWS_PATH, f'news{self.today}.json')
        self.url = 'http://api.mediastack.com/v1/news'
        self.params = {
            'access_key': 'Your API key',
            'languages': 'en',
            'sort': 'published_desc',
            'limit': 50,
            'keywords': ['cafe', 'coffee']
        }

    def get_response(self):
        new = []
        if self.check_file():
            os.remove(self.filename)
        resp = requests.get(url=self.url, params=self.params)
        for (index, i) in enumerate(resp.json()['data']):
            if i['image'] is not None and 'https://www.youtube.com' not in i['image']:
                if i['author'] is not None:
                    if i['author'] != '' or i['author'] != 'None':
                        local_dict = {
                            'author': i['author'],
                            'title': i['title'],
                            'description': i['description'],
                            'url': i['url'],
                            'image':i['image'],
                        }
                        new.append(local_dict)

        with open(self.filename, 'w') as json_file:
            json.dump(new, json_file)

    def check_file(self):
        try:
            with open(self.filename, 'r') as file:
                return True
        except FileNotFoundError:
            return False

    def read_news(self):
        with open(self.filename, 'r') as file:
            data_dict = json.load(file)
            return data_dict

    def check_date(self):
        creation_timestamp = os.path.getctime(self.filename)
        creation_date = datetime.datetime.fromtimestamp(creation_timestamp)
        creation_date = creation_date.date()
        today = datetime.date.today()

        if today == creation_date:

            return True
        else:

            return False
