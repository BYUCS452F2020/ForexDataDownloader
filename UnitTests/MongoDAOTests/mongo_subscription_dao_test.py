import unittest
from MongoDAO.mongo_subscription_dao import MongoSubscriptionDAO


# TODO: add more tests for failures, etc.
class MongoSubscriptionDaoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mongo_subscription_dao = MongoSubscriptionDAO()

    def test_insert_new_subscription_user_id_fail(self):
        success, error_message = self.mongo_subscription_dao.insert_new_subscription(58, 'Basic', 5.99)

        self.assertEqual(error_message, 'Invalid parameters used when trying to add a new subscription')

    def test_insert_new_subscription_subscription_type_fail(self):
        success, error_message = self.mongo_subscription_dao.insert_new_subscription('123', 'blah', 5.99)

        self.assertEqual(error_message, 'Invalid parameters used when trying to add a new subscription')

    def test_insert_new_subscription_subscription_cost_fail(self):
        success, error_message = self.mongo_subscription_dao.insert_new_subscription('123', 'Basic', '5.99')

        self.assertEqual(error_message, 'Invalid parameters used when trying to add a new subscription')

    def test_insert_new_subscription_success(self):
        success, error_message = self.mongo_subscription_dao.insert_new_subscription('123', 'Basic', 5.99)

        self.assertTrue(success)

    def test_update_subscription_user_id_fail(self):
        success, error_message = self.mongo_subscription_dao.update_subscription(58, 'Basic', 5.99)

        self.assertEqual(error_message, 'Invalid parameters used when trying to update a subscription')

    def test_update_subscription_subscription_type_fail(self):
        success, error_message = self.mongo_subscription_dao.update_subscription('123', 'blah', 5.99)

        self.assertEqual(error_message, 'Invalid parameters used when trying to update a subscription')

    def test_update_subscription_subscription_cost_fail(self):
        success, error_message = self.mongo_subscription_dao.update_subscription('123', 'Basic', '5.99')

        self.assertEqual(error_message, 'Invalid parameters used when trying to update a subscription')

    def test_update_subscription_success(self):
        success1, error_message1 = self.mongo_subscription_dao.insert_new_subscription('1234', 'Basic', 5.99)
        success2, error_message2 = self.mongo_subscription_dao.update_subscription('1234', 'Premium', 7.99)

        self.assertTrue(success1 and success2)

        monthly_bill, error_message3 = self.mongo_subscription_dao.get_monthly_bill('1234')

        self.assertEqual(monthly_bill, 7.99)

    def test_get_monthly_bill_user_id_fail(self):
        success, error_message = self.mongo_subscription_dao.get_monthly_bill(123)

        self.assertEqual(error_message, 'Invalid user ID; should be a string')

    def test_get_monthly_bill_success(self):
        success1, error_message1 = self.mongo_subscription_dao.insert_new_subscription('71', 'Premium', 15.99)
        monthly_bill, error_message2 = self.mongo_subscription_dao.get_monthly_bill('71')

        self.assertEqual(monthly_bill, 15.99)


if __name__ == '__main__':
    unittest.main()
