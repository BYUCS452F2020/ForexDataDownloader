import pymongo


class MongoPairsFollowedDAO:
    def __init__(self):
        mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

        self.mongo_db = mongo_client['forex']

        self.pairs_followed_collection = self.mongo_db['pairs_followed']

    def insert_new_pair_followed(self, user_id, currency_name):
        pair_followed = self.pairs_followed_collection.insert_one({'user_id': user_id, 'currency_name': currency_name})

        return True, None

    def remove_pair_followed(self, user_id, currency_name):
        pair_followed = self.pairs_followed_collection.delete_one({'user_id': user_id, 'currency_name': currency_name})

        return True, None

    def get_pairs_followed(self, user_id):
        pairs_followed = self.pairs_followed_collection.find({'user_id': user_id})

        pairs = []

        for pair in pairs_followed:
            pairs.append(pair['currency_name'])

        return pairs, None
