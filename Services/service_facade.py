from Services.CurrencyPair.currency_pair_service import CurrencyPairService
from Services.DataDownload.data_download_service import DataDownloadService
from Services.Subscription.subscription_service import SubscriptionService
from Services.User.user_service import UserService


# TODO: add docs
class ServiceFacade:
    def __init__(self):
        self.currency_pair_service = CurrencyPairService()
        self.data_download_service = DataDownloadService()
        self.subscription_service = SubscriptionService()
        self.user_service = UserService()
        self.subscription_types_and_costs = {'Basic': 5.99, 'Premium': 9.99}

    def get_available_currency_pairs(self):
        return self.currency_pair_service.get_available_currency_pairs()

    def get_pairs_followed_for_user(self, user_id):
        return self.currency_pair_service.get_pairs_followed_for_user(user_id)

    def update_pairs_followed_for_user(self, user_id, currency_pair_name):
        pairs_left, error_message = self.get_followed_pairs_left_for_user(user_id)

        if error_message is not None:
            return error_message

        pairs_left = pairs_left[0]

        if pairs_left == -1 or pairs_left > 0:
            first_update_success, first_error_message = self.currency_pair_service.update_pairs_followed_for_user(user_id, currency_pair_name)
            second_update_success, second_error_message = self.decrement_followed_pairs_left_for_user(user_id)

            if first_update_success and second_update_success:
                return_message = 'Successfully updated pairs followed'

            else:
                return_message = 'Failed to update pairs followed'

        else:
            return_message = 'Cannot update pairs followed for user - monthly limit reached'

        return return_message

    def get_followed_pairs_left_for_user(self, user_id):
        return self.currency_pair_service.get_followed_pairs_left_for_user(user_id)

    def update_followed_pairs_left_for_user(self, user_id, num_pairs_available):
        return self.currency_pair_service.update_followed_pairs_left_for_user(user_id, num_pairs_available)

    def insert_followed_pairs_left_for_user(self, user_id, num_pairs_available):
        return self.currency_pair_service.insert_followed_pairs_left_for_user(user_id, num_pairs_available)

    def decrement_followed_pairs_left_for_user(self, user_id):
        return self.currency_pair_service.decrement_followed_pairs_left(user_id)

    def get_historical_data(self, currency_pair, time_frame_granularity, from_time, to_time):
        candles, error_message = self.data_download_service.get_historical_data(currency_pair, time_frame_granularity,
                                                                                from_time, to_time)

        return candles, error_message

    def create_subscription(self, user_id, subscription_type):
        if subscription_type in self.subscription_types_and_costs:
            subscription_cost = self.subscription_types_and_costs[subscription_type]
            return self.subscription_service.create_subscription(user_id, subscription_type, subscription_cost)

        else:
            return False, 'Invalid subscription type'

    def update_subscription(self, user_id, subscription_type):
        if subscription_type in self.subscription_types_and_costs:
            subscription_cost = self.subscription_types_and_costs[subscription_type]
            first_success, first_error_message = self.subscription_service.update_subscription(user_id,
                                                                                               subscription_type,
                                                                                               subscription_cost)
            second_success = False

            if first_success:
                num_pairs_available = -1 if subscription_type == 'Premium' else 5
                second_success, second_error_message = self.update_followed_pairs_left_for_user(user_id,
                                                                                                num_pairs_available)

            return 'Updated subscription' if first_success and second_success else 'Failed to update subscription'

        else:
            return 'Invalid subscription type'

    def create_user(self, username, first_name, last_name, password, subscription_type):
        user_id, first_error_message = self.user_service.create_user(username, first_name, last_name, password)

        if first_error_message is not None:
            return None, first_error_message

        first_success, second_error_message = self.create_subscription(user_id, subscription_type)

        if not first_success:
            return None, second_error_message

        num_pairs_available = -1 if subscription_type == 'Premium' else 5
        second_success, third_error_message = self.insert_followed_pairs_left_for_user(user_id, num_pairs_available)

        if not second_success:
            return None, third_error_message

        return user_id, third_error_message

    def login(self, username, password):
        return self.user_service.login(username, password)

    def get_monthly_bill(self, user_id):
        return self.subscription_service.get_monthly_bill(user_id)
