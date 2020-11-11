import unittest
from MongoDAO.mongo_pairs_followed_dao import MongoPairsFollowedDAO


# TODO: add more tests for failures, etc.
class PairsFollowedDaoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mongo_pairs_followed_dao = MongoPairsFollowedDAO()

    def test_insert_new_pair_followed(self):
        success, error_message = self.mongo_pairs_followed_dao.insert_new_pair_followed('user_id123', 'curr_pair123')

        self.assertTrue(success)

    def test_get_pairs_followed(self):
        self.mongo_pairs_followed_dao.insert_new_pair_followed('abc', 'EUR/USD')
        pairs_followed, error_message = self.mongo_pairs_followed_dao.get_pairs_followed('abc')

        for pair in pairs_followed:
            self.assertEqual(pair, 'EUR/USD')

    def test_remove_pair_followed(self):
        self.mongo_pairs_followed_dao.insert_new_pair_followed('xyz', 'EUR/USD')
        self.mongo_pairs_followed_dao.insert_new_pair_followed('xyz', 'USD/CAD')
        success, error_message = self.mongo_pairs_followed_dao.remove_pair_followed('xyz', 'EUR/USD')

        self.assertTrue(success)

        pairs_followed, error_message = self.mongo_pairs_followed_dao.get_pairs_followed('xyz')

        self.assertTrue(len(pairs_followed) == 1)
        self.assertEqual(pairs_followed[-1], 'USD/CAD')

if __name__ == '__main__':
    unittest.main()
