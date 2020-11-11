import pymongo
from bson import ObjectId


class MongoCurrencyPairDAO:
    def __init__(self):
        mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

        self.mongo_db = mongo_client['forex']

        self.currency_pairs_collection = self.mongo_db['currency_pairs']

    def add_currency_pair(self, currency_name):
        new_currency_pair = self.currency_pairs_collection.insert_one({'currency_name': currency_name})

        return True, None

    def get_currency_pair(self, currency_id):
        currency_pair = self.currency_pairs_collection.find_one({'_id': ObjectId(currency_id)})

        return currency_pair, None

    def get_all_currency_pairs(self):
        all_currency_pairs = self.currency_pairs_collection.find({})

        return all_currency_pairs, None
