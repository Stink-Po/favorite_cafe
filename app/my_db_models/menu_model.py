from pymongo import MongoClient
from bson.objectid import ObjectId


class CafeMenu:
    """ A MongoDb Table For Storing Café Menu items and price With pymongo """

    def __init__(self, ):
        """
        initialise the AWS mongodb for storing café menu details
        """
        self.client = MongoClient(
            'mongodb+srv://stink:ihj5BxK8xsbNxUho@cafedb.08ofdiv.mongodb.net/?retryWrites=true&w=majority')
        self.db = self.client['cafe']
        self.collection = self.db['cafe']
        self.post = {}

    def post_maker(self, menu_items: list, prices: list):
        """
        Commit Menu items in Mongodb database
        :return: _id of the stored menu items on mongo db to stored of café table in mysql
        """
        self.make_dict(menu_items=menu_items, prices=prices)
        cafeid = self.collection.insert_one(self.post).inserted_id
        return cafeid

    def find_cafe_menu(self, _id):
        """
        :param _id: id of the mongodb row that stored in Mysql Café table
        :return: row that contain data of a café Menu and prices
        """
        results = []
        for (k, v) in self.collection.find_one({'_id': ObjectId(_id)}).items():
            if k != '_id':
                results.append(v)
                print(v)
        return results

    def make_dict(self, menu_items: list, prices: list):

        if len(menu_items) > len(prices):
            length = len(prices)
        elif len(prices) > len(menu_items):
            length = len(menu_items)
        else:
            length = len(menu_items)

        for i in range(length):
            if menu_items[i] != '' and prices[i] != '':
                local_dict = {
                    'menu_item': str(menu_items[i]),
                    'item_price': str(prices[i])
                }
                self.post[str(i)] = local_dict
