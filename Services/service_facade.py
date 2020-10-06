from Services.CurrencyPair.currency_pair_service import CurrencyPairService
from Services.DataDownload.data_download_service import DataDownloadService
from Services.Subscription.subscription_service import SubscriptionService
from Services.User.user_service import UserService
import math


# TODO: add documentation/comments once fully implemented
class ServiceFacade:
    def __init__(self):
        self.currency_pair_service = CurrencyPairService()
        self.data_download_service = DataDownloadService()
        self.subscription_service = SubscriptionService()
        self.user_service = UserService()
        self.subscription_types_and_costs = {'Basic': 5.99, 'Premium': 9.99}

    # TODO: finish and add docs when currency pair service is fully implemented
    def get_available_currency_pairs(self):
        available_pairs = self.currency_pair_service.get_available_currency_pairs()

    # TODO: finish and add docs when currency pair service is fully implemented
    def get_pairs_followed_for_user(self, user_id):
        pairs_followed_for_user = self.currency_pair_service.get_pairs_followed_for_user(user_id)

    # TODO: finish and add docs when currency pair service is fully implemented
    def update_pairs_followed_for_user(self, user_id, currency_pair_name):
        pairs_left = self.get_followed_pairs_left_for_user(user_id)

        if pairs_left != -math.inf and pairs_left > 0:
            self.currency_pair_service.update_pairs_followed_for_user(user_id, currency_pair_name)
            self.update_followed_pairs_left_for_user(user_id)

    # TODO: finish and add docs when currency pair service is fully implemented
    def get_followed_pairs_left_for_user(self, user_id):
        pairs_left = self.currency_pair_service.get_followed_pairs_left_for_user(user_id)

    # TODO: finish and add docs when currency pair service is fully implemented
    def update_followed_pairs_left_for_user(self, user_id):
        change_amount = 1
        self.currency_pair_service.update_pairs_followed_for_user(user_id, change_amount)

    # TODO: test this and possibly change the format of the returned candle data
    def get_historical_data(self, currency_pair, time_frame_granularity, from_time, to_time):
        candles, error_message = self.data_download_service.get_historical_data(currency_pair, time_frame_granularity,
                                                                                from_time, to_time)

        return candles, error_message

    # TODO: test this once the subscription service is fully implemented and handle the error
    def create_subscription(self, user_id, subscription_type):
        if subscription_type in self.subscription_types_and_costs:
            subscription_cost = self.subscription_types_and_costs[subscription_type]
            self.subscription_service.create_subscription(user_id, subscription_type, subscription_cost)

        else:
            # error  # TODO: change this
            pass

    # TODO: test this once the subscription service is fully implemented and handle the error
    def update_subscription(self, user_id, subscription_type):
        if subscription_type in self.subscription_types_and_costs:
            subscription_cost = self.subscription_types_and_costs[subscription_type]
            self.subscription_service.update_subscription(user_id, subscription_type, subscription_cost)

        else:
            # error  # TODO: change this
            pass

    # TODO: finish and add docs when user service is fully implemented
    def create_user(self, username, first_name, last_name):
        self.user_service.create_user(username, first_name, last_name)

    # TODO: finish and add docs when user service is fully implemented
    def login(self, username):
        self.user_service.login(username)
