import unittest
from MongoDAO.mongo_currency_pair_dao import MongoCurrencyPairDAO


# TODO: add more tests for failures, etc.
class MongoCurrencyPairDaoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mongo_currency_pair_dao = MongoCurrencyPairDAO()

    # EUR/USD, USD/JPY, GBP/USD, USD/CHF, AUD/USD, USD/CAD, NZD/USD
    def test_insert_new_currency_pair(self):
        success, error_message = self.mongo_currency_pair_dao.add_currency_pair('EUR/USD')
        self.assertEqual(error_message, None)
        success, error_message = self.mongo_currency_pair_dao.add_currency_pair('USD/JPY')
        self.assertEqual(error_message, None)
        success, error_message = self.mongo_currency_pair_dao.add_currency_pair('GBP/USD')
        self.assertEqual(error_message, None)
        success, error_message = self.mongo_currency_pair_dao.add_currency_pair('AUD/USD')
        self.assertEqual(error_message, None)
        success, error_message = self.mongo_currency_pair_dao.add_currency_pair('USD/CAD')
        self.assertEqual(error_message, None)
        success, error_message = self.mongo_currency_pair_dao.add_currency_pair('NZD/USD')
        self.assertEqual(error_message, None)

    def test_retrieve_data(self):
        pairs, error_message = self.mongo_currency_pair_dao.get_all_currency_pairs()

        self.assertIsNotNone(pairs)

        for pair in pairs:
            print(pair)


if __name__ == '__main__':
    unittest.main()
