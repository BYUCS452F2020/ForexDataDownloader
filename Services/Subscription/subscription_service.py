from MongoDAO.mongo_subscription_dao import MongoSubscriptionDAO


# TODO: add docs
class SubscriptionService:
    def __init__(self):
        self.subscription_dao = MongoSubscriptionDAO()

    def create_subscription(self, user_id, subscription_type, subscription_cost):
        return self.subscription_dao.insert_new_subscription(user_id, subscription_type, subscription_cost)

    def update_subscription(self, user_id, subscription_type, subscription_cost):
        return self.subscription_dao.update_subscription(user_id, subscription_type, subscription_cost)

    def get_monthly_bill(self, user_id):
        return self.subscription_dao.get_monthly_bill(user_id)
