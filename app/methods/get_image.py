from pexels_api import API
import random

PEXELS_API_KEY = "Your Pexels API key"


class GetPhoto:
    def __init__(self, search_object: str):
        self.api = API(PEXELS_API_KEY)
        self.results = []
        self.final = []
        self.object = search_object
        self.get()

    def get(self):
        self.api.search(self.object, results_per_page=30, page=2)
        photos = self.api.get_entries()
        if len(photos) != 0:
            self.results = [pic.large2x for pic in photos]
        else:
            self.api.search("cafe")
            photos = self.api.get_entries()
            self.results = [pic.medium for pic in photos]
        final = [random.choice(self.results) for i in range(3)]
        random.shuffle(final)
        self.final = final
        return self.final
