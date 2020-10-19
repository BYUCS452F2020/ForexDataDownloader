import unittest
from Services.service_facade import ServiceFacade
from Database.database_clearer import DatabaseClearer


class ServiceFacadeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.service_facade = ServiceFacade()

    def test_get_available_currency_pairs(self):
        pairs, error_message = self.service_facade.get_available_currency_pairs()

        self.assertIsNotNone(pairs)
        self.assertEqual(len(pairs), 6)
        self.assertIsNone(error_message)

    def test_create_user(self):
        DatabaseClearer.clear_database()
        user_id, error_message = self.service_facade.create_user('bob5', 'Bob', 'Belcher', 'bobsburgers123', 'Basic')

        self.assertIsNotNone(user_id)
        self.assertIsNone(error_message)

    def test_login(self):
        user_id, error_message = self.service_facade.login('bob5', 'bobsburgers123')

        self.assertIsNotNone(user_id)
        self.assertIsNone(error_message)

    def test_get_monthly_bill(self):
        user_id, error_message1 = self.service_facade.login('bob5', 'bobsburgers123')

        self.assertIsNotNone(user_id)
        self.assertIsNone(error_message1)

        monthly_bill, error_message2 = self.service_facade.get_monthly_bill(user_id[0])

        self.assertIsNotNone(monthly_bill)
        self.assertEqual(monthly_bill[0], 5.99)
        self.assertIsNone(error_message2)

    def test_update_pairs_followed_for_user(self):
        user_id, error_message1 = self.service_facade.login('bob5', 'bobsburgers123')

        self.assertIsNotNone(user_id)
        self.assertIsNone(error_message1)

        return_message = self.service_facade.update_pairs_followed_for_user(user_id[0], 'EUR/USD')

        self.assertEqual(return_message, 'Successfully updated pairs followed')

    def test_get_followed_pairs_left_for_user(self):
        user_id, error_message1 = self.service_facade.login('bob5', 'bobsburgers123')

        self.assertIsNotNone(user_id)
        self.assertIsNone(error_message1)

        pairs_left, error_message2 = self.service_facade.get_followed_pairs_left_for_user(user_id[0])

        self.assertEqual(pairs_left[0], 4)
        self.assertIsNone(error_message2)

    def test_get_pairs_followed_for_user(self):
        user_id, error_message1 = self.service_facade.login('bob5', 'bobsburgers123')

        self.assertIsNotNone(user_id)
        self.assertIsNone(error_message1)

        pairs_followed, error_message2 = self.service_facade.get_pairs_followed_for_user(user_id[0])

        self.assertEqual(len(pairs_followed), 0)
        self.assertIsNone(error_message2)

    def test_update_followed_pairs_left_for_user(self):
        user_id, error_message1 = self.service_facade.login('bob5', 'bobsburgers123')

        self.assertIsNotNone(user_id)
        self.assertIsNone(error_message1)

        success1, error_message2 = self.service_facade.update_followed_pairs_left_for_user(user_id[0], 10)

        self.assertTrue(success1)
        self.assertIsNone(error_message2)

        pairs_left, error_message2 = self.service_facade.get_followed_pairs_left_for_user(user_id[0])

        self.assertEqual(pairs_left[0], 10)
        self.assertIsNone(error_message2)

    def test_decrement_followed_pairs_left_for_user(self):
        user_id, error_message1 = self.service_facade.login('bob5', 'bobsburgers123')

        self.assertIsNotNone(user_id)
        self.assertIsNone(error_message1)

        success1, error_message2 = self.service_facade.decrement_followed_pairs_left_for_user(user_id[0])

        self.assertTrue(success1)
        self.assertIsNone(error_message2)

        pairs_left, error_message2 = self.service_facade.get_followed_pairs_left_for_user(user_id[0])

        self.assertEqual(pairs_left[0], 4)
        self.assertIsNone(error_message2)

    def test_get_historical_data(self):
        candles_df, error_message = self.service_facade.get_historical_data('EUR_USD', 'H1', '2020-09-15 00:00:00',
                                                                            '2020-09-15 12:00:00')

        self.assertEqual(candles_df.shape, (12, 9))

    def test_update_subscription(self):
        user_id, error_message1 = self.service_facade.login('bob5', 'bobsburgers123')

        self.assertIsNotNone(user_id)
        self.assertIsNone(error_message1)

        return_message = self.service_facade.update_subscription(user_id[0], 'Premium')

        self.assertEqual(return_message, 'Updated subscription')

        monthly_bill, error_message2 = self.service_facade.get_monthly_bill(user_id[0])

        self.assertEqual(monthly_bill[0], 9.99)
        self.assertIsNone(error_message2)

    def test_clean_up_db(self):
        DatabaseClearer.clear_database()


if __name__ == '__main__':
    unittest.main()
