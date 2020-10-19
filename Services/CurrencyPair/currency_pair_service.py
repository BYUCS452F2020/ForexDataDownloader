from DAO.currency_pair_dao import CurrencyPairDAO
from DAO.followed_pairs_left_dao import FollowedPairsLeftDAO
from DAO.pairs_followed_dao import PairsFollowedDAO


# TODO: add docs
class CurrencyPairService:
    def __init__(self):
        self.currency_pair_dao = CurrencyPairDAO()
        self.followed_pairs_left_dao = FollowedPairsLeftDAO()
        self.pair_followed_dao = PairsFollowedDAO()

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
