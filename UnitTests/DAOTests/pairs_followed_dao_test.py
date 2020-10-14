import unittest
from DAO.pairs_followed_dao import PairsFollowedDAO

# TODO: add more tests for failures, etc.
class PairsFollowedDaoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.pairs_followed_dao = PairsFollowedDAO()

    def test_insert_new_pair_follwed(self):
        self.pairs_followed_dao._create_pairs_followed_table()

        success, error_message = self.pairs_followed_dao.insert_new_pair_followed('user_id123', 'curr_pair123')

        self.assertTrue(success)

    def test_get_pair_followed(self):
        self.pairs_followed_dao._create_pairs_followed_table()

        self.pairs_followed_dao.insert_new_pair_followed('user_id123', 'curr_pair123')
        success, error_message = self.pairs_followed_dao.get_pairs_followed('user_id123')

        self.assertEqual(success[0][2], 'curr_pair123')

        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()
