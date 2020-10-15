import unittest
from DAO.followed_pairs_left_dao import FollowedPairsLeftDAO


# TODO: add more tests for failures, etc.
class SubscriptionDaoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.followed_pairs_left_dao = FollowedPairsLeftDAO()

    def test_insert_new_followed_pairs_left_user_id_fail(self):
        self.followed_pairs_left_dao._create_followed_pairs_left_table()

        success, error_message = self.followed_pairs_left_dao.insert_new_followed_pairs_left(58, 5)

        self.assertEqual(error_message, 'Invalid parameters used when trying to add a new followed pairs left')

    def test_insert_new_followed_pairs_left_num_pairs_available_fail(self):
        self.followed_pairs_left_dao._create_followed_pairs_left_table()

        success, error_message = self.followed_pairs_left_dao.insert_new_followed_pairs_left('abc', '5')

        self.assertEqual(error_message, 'Invalid parameters used when trying to add a new followed pairs left')

    def test_insert_new_followed_pairs_left_success(self):
        self.followed_pairs_left_dao._create_followed_pairs_left_table()

        success, error_message = self.followed_pairs_left_dao.insert_new_followed_pairs_left('abc', 5)

        self.assertTrue(success)

    def test_update_followed_pairs_left_user_id_fail(self):
        self.followed_pairs_left_dao._create_followed_pairs_left_table()

        success, error_message = self.followed_pairs_left_dao.update_followed_pairs_left(58, 5)

        self.assertEqual(error_message, 'Invalid parameters used when trying to update a followed pairs left')

    def test_update_followed_pairs_left_num_pairs_available_fail(self):
        self.followed_pairs_left_dao._create_followed_pairs_left_table()

        success, error_message = self.followed_pairs_left_dao.update_followed_pairs_left('abc', '5')

        self.assertEqual(error_message, 'Invalid parameters used when trying to update a followed pairs left')

    def test_update_followed_pairs_left_success(self):
        self.followed_pairs_left_dao._create_followed_pairs_left_table()

        success1, error_message1 = self.followed_pairs_left_dao.insert_new_followed_pairs_left('123', 5)
        success2, error_message2 = self.followed_pairs_left_dao.update_followed_pairs_left('123', 27)

        self.assertTrue(success1 and success2)

        num_pairs_available, error_message3 = self.followed_pairs_left_dao.get_followed_pairs_left('123')

        self.assertEqual(num_pairs_available, (27,))

    def test_decrement_followed_pairs_left_user_id_fail(self):
        self.followed_pairs_left_dao._create_followed_pairs_left_table()

        success, error_message = self.followed_pairs_left_dao.decrement_followed_pairs_left(45)

        self.assertEqual(error_message, 'Invalid user ID; should be a string')

    def test_decrement_followed_pairs_left_success(self):
        self.followed_pairs_left_dao._create_followed_pairs_left_table()

        success1, error_message1 = self.followed_pairs_left_dao.insert_new_followed_pairs_left('123', 5)
        success2, error_message2 = self.followed_pairs_left_dao.decrement_followed_pairs_left('123')

        self.assertTrue(success1 and success2)

        num_pairs_available, error_message3 = self.followed_pairs_left_dao.get_followed_pairs_left('123')

        self.assertEqual(num_pairs_available, (4,))

    def test_decrement_zero_followed_pairs_left(self):
        self.followed_pairs_left_dao._create_followed_pairs_left_table()

        success1, error_message1 = self.followed_pairs_left_dao.insert_new_followed_pairs_left('123', 0)
        success2, error_message2 = self.followed_pairs_left_dao.decrement_followed_pairs_left('123')

        self.assertTrue(success1 and success2)

        num_pairs_available, error_message3 = self.followed_pairs_left_dao.get_followed_pairs_left('123')

        self.assertEqual(num_pairs_available, (0,))

    def test_decrement_negative_followed_pairs_left(self):
        self.followed_pairs_left_dao._create_followed_pairs_left_table()

        success1, error_message1 = self.followed_pairs_left_dao.insert_new_followed_pairs_left('123', -1)
        success2, error_message2 = self.followed_pairs_left_dao.decrement_followed_pairs_left('123')

        self.assertTrue(success1 and success2)

        num_pairs_available, error_message3 = self.followed_pairs_left_dao.get_followed_pairs_left('123')

        self.assertEqual(num_pairs_available, (-1,))

    def test_get_followed_pairs_left_user_id_fail(self):
        self.followed_pairs_left_dao._create_followed_pairs_left_table()

        success, error_message = self.followed_pairs_left_dao.get_followed_pairs_left(45)

        self.assertEqual(error_message, 'Invalid user ID; should be a string')

    def test_get_followed_pairs_left_success(self):
        self.followed_pairs_left_dao._create_followed_pairs_left_table()

        success1, error_message1 = self.followed_pairs_left_dao.insert_new_followed_pairs_left('123', 100)
        num_pairs_available, error_message = self.followed_pairs_left_dao.get_followed_pairs_left('123')

        self.assertEqual(num_pairs_available, (100,))



if __name__ == '__main__':
    unittest.main()
