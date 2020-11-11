import pymongo


class MongoFollowedPairsLeftDAO:
    def __init__(self):
        mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

        self.mongo_db = mongo_client['forex']

        self.followed_pairs_left_collection = self.mongo_db['followed_pairs_left']

    def _check_followed_pairs_left_parameters(self, user_id, num_pairs_available):
        return isinstance(user_id, str) and isinstance(num_pairs_available, int)

    def insert_new_followed_pairs_left(self, user_id, num_pairs_available):
        valid_parameters = self._check_followed_pairs_left_parameters(user_id, num_pairs_available)

        if not valid_parameters:
            return False, 'Invalid parameters used when trying to add a new followed pairs left'

        followed_pairs_left = self.followed_pairs_left_collection.insert_one({'user_id': user_id,
                                                                              'num_pairs_available':
                                                                                  num_pairs_available})

        return True, None

    def update_followed_pairs_left(self, user_id, num_pairs_available):
        valid_parameters = self._check_followed_pairs_left_parameters(user_id, num_pairs_available)

        if not valid_parameters:
            return False, 'Invalid parameters used when trying to update a followed pairs left'

        followed_pairs_left = self.followed_pairs_left_collection.update_one({'user_id': user_id},
                                                                             {'$set': {'num_pairs_available':
                                                                              num_pairs_available}})

        return True, None

    def decrement_followed_pairs_left(self, user_id):
        if not isinstance(user_id, str):
            return False, 'Invalid user ID; should be a string'

        followed_pairs_left = self.followed_pairs_left_collection.update_one({'user_id': user_id,
                                                                              'num_pairs_available': {'$gt': 0}},
                                                                             {'$inc': {'num_pairs_available': -1}})

        return True, None

    def get_followed_pairs_left(self, user_id):
        if not isinstance(user_id, str):
            return None, 'Invalid user ID; should be a string'

        followed_pairs_left = self.followed_pairs_left_collection.find_one({'user_id': user_id}, {'_id': 0,
                                                                                                  'user_id': 1,
                                                                                                  'num_pairs_available':
                                                                                                      1})

        num_pairs_available = followed_pairs_left['num_pairs_available']

        return num_pairs_available, None
