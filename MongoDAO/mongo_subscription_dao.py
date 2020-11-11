import pymongo


class MongoSubscriptionDAO:
    def __init__(self):
        mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

        self.mongo_db = mongo_client['forex']

        self.subscriptions_collection = self.mongo_db['subscriptions']

        # A list of available subscription types
        self.available_subscription_types = ['Basic', 'Premium']

    def _check_subscription_parameters(self, user_id, subscription_type, subscription_cost):
        return isinstance(user_id, str) and isinstance(subscription_type, str) and isinstance(subscription_cost, float) \
               and subscription_type in self.available_subscription_types

    def insert_new_subscription(self, user_id, subscription_type, subscription_cost):
        valid_parameters = self._check_subscription_parameters(user_id, subscription_type, subscription_cost)

        if not valid_parameters:
            return False, 'Invalid parameters used when trying to add a new subscription'

        subscription = self.subscriptions_collection.insert_one({'user_id': user_id,
                                                                 'subscription_type': subscription_type,
                                                                 'monthly_cost': subscription_cost})

        return True, None

    def update_subscription(self, user_id, subscription_type, subscription_cost):
        valid_parameters = self._check_subscription_parameters(user_id, subscription_type, subscription_cost)

        if not valid_parameters:
            return False, 'Invalid parameters used when trying to update a subscription'

        subscription = self.subscriptions_collection.update_one({'user_id': user_id},
                                                                {'$set': {'monthly_cost': subscription_cost,
                                                                          'subscription_type': subscription_type}})

        return True, None

    def get_monthly_bill(self, user_id):
        if not isinstance(user_id, str):
            return None, 'Invalid user ID; should be a string'

        subscription = self.subscriptions_collection.find_one({'user_id': user_id}, {'_id': 0, 'user_id': 1,
                                                                                     'subscription_type': 1,
                                                                                     'monthly_cost': 1})

        return subscription['monthly_cost'], None
