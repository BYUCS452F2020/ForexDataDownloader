import unittest
from DAO.currency_pair_dao import CurrencyPairDAO


# TODO: add more tests for failures, etc.
class CurrencyPairDaoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.currency_pair_dao = CurrencyPairDAO()

    #EUR/USD, USD/JPY, GBP/USD, USD/CHF, AUD/USD, USD/CAD, NZD/USD
    def test_insert_new_currency_pair(self):
        self.currency_pair_dao._create_currency_pairs_table()

        success, error_message = self.currency_pair_dao.add_currency_pair('EUR/USD')

        self.assertEqual(error_message, None)

    def test_retrieve_data(self):
        self.currency_pair_dao._create_currency_pairs_table()

        self.currency_pair_dao.add_currency_pair('EUR/USD')
        self.currency_pair_dao.add_currency_pair('USD/JPY')
        self.currency_pair_dao.add_currency_pair('GBP/USD')
        self.currency_pair_dao.add_currency_pair('USD/CHF')
        self.currency_pair_dao.add_currency_pair('AUD/USD')
        self.currency_pair_dao.add_currency_pair('USD/CAD')
        self.currency_pair_dao.add_currency_pair('NZD/USD')

        pairs, error_message = self.currency_pair_dao.get_all_currency_pairs()

        self.assertIsNotNone(pairs)


if __name__ == '__main__':
    unittest.main()
