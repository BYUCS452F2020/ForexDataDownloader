from MongoDAO.mongo_currency_pair_dao import MongoCurrencyPairDAO
from MongoDAO.mongo_followed_pairs_left_dao import MongoFollowedPairsLeftDAO
from MongoDAO.mongo_pairs_followed_dao import MongoPairsFollowedDAO


# TODO: add docs
class CurrencyPairService:
    def __init__(self):
        self.currency_pair_dao = MongoCurrencyPairDAO()
        self.followed_pairs_left_dao = MongoFollowedPairsLeftDAO()
        self.pair_followed_dao = MongoPairsFollowedDAO()

    def get_available_currency_pairs(self):
        return self.currency_pair_dao.get_all_currency_pairs()

    def get_pairs_followed_for_user(self, user_id):
        return self.pair_followed_dao.get_pairs_followed(user_id)

    def update_pairs_followed_for_user(self, user_id, currency_pair_name):
        return self.pair_followed_dao.insert_new_pair_followed(user_id, currency_pair_name)

    def get_followed_pairs_left_for_user(self, user_id):
        return self.followed_pairs_left_dao.get_followed_pairs_left(user_id)

    def update_followed_pairs_left_for_user(self, user_id, num_pairs_available):
        return self.followed_pairs_left_dao.update_followed_pairs_left(user_id, num_pairs_available)

    def insert_followed_pairs_left_for_user(self, user_id, num_pairs_available):
        return self.followed_pairs_left_dao.insert_new_followed_pairs_left(user_id, num_pairs_available)

    def decrement_followed_pairs_left(self, user_id):
        return self.followed_pairs_left_dao.decrement_followed_pairs_left(user_id)
