# TODO: get imports once the needed modules are implemented


# TODO: add docs once service is implemented
class CurrencyPairService:
    def __init__(self):
        self.pair_followed_dao = None  # TODO: get the actual pair followed dao once it's implemented
        self.followed_pairs_left_dao = None  # TODO: get the actual followed pairs left dao once it's implemented

    # TODO: implement and add docs when currency pairs dao is implemented
    def get_available_currency_pairs(self):
        pass

    # TODO: implement and add docs when pair followed dao is implemented
    def get_pairs_followed_for_user(self, user_id):
        pass

    # TODO: implement and add docs when pair followed dao is implemented
    def update_pairs_followed_for_user(self, user_id, currency_pair_id):
        pass

    # TODO: implement and add docs when followed pairs left dao is implemented
    def get_followed_pairs_left_for_user(self, user_id):
        pass

    # TODO: implement and add docs when followed pairs left dao is implemented
    def update_followed_pairs_left_for_user(self, user_id, change_amount):
        pass
