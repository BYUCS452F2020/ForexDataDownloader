import unittest
from MongoDAO.mongo_followed_pairs_left_dao import MongoFollowedPairsLeftDAO


# TODO: add more tests for failures, etc.
class SubscriptionDaoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mongo_followed_pairs_left_dao = MongoFollowedPairsLeftDAO()

    def test_insert_new_followed_pairs_left_user_id_fail(self):
        success, error_message = self.mongo_followed_pairs_left_dao.insert_new_followed_pairs_left(58, 5)

        self.assertEqual(error_message, 'Invalid parameters used when trying to add a new followed pairs left')

    def test_insert_new_followed_pairs_left_num_pairs_available_fail(self):
        success, error_message = self.mongo_followed_pairs_left_dao.insert_new_followed_pairs_left('abc', '5')

        self.assertEqual(error_message, 'Invalid parameters used when trying to add a new followed pairs left')

    def test_insert_new_followed_pairs_left_success(self):
        success, error_message = self.mongo_followed_pairs_left_dao.insert_new_followed_pairs_left('abc', 5)

        self.assertTrue(success)

    def test_update_followed_pairs_left_user_id_fail(self):
        success, error_message = self.mongo_followed_pairs_left_dao.update_followed_pairs_left(58, 5)

        self.assertEqual(error_message, 'Invalid parameters used when trying to update a followed pairs left')

    def test_update_followed_pairs_left_num_pairs_available_fail(self):
        success, error_message = self.mongo_followed_pairs_left_dao.update_followed_pairs_left('abc', '5')

        self.assertEqual(error_message, 'Invalid parameters used when trying to update a followed pairs left')

    def test_update_followed_pairs_left_success(self):
        success1, error_message1 = self.mongo_followed_pairs_left_dao.insert_new_followed_pairs_left('123', 5)
        success2, error_message2 = self.mongo_followed_pairs_left_dao.update_followed_pairs_left('123', 27)

        self.assertTrue(success1 and success2)

        num_pairs_available, error_message3 = self.mongo_followed_pairs_left_dao.get_followed_pairs_left('123')

        self.assertEqual(num_pairs_available, 27)

    def test_decrement_followed_pairs_left_user_id_fail(self):
        success, error_message = self.mongo_followed_pairs_left_dao.decrement_followed_pairs_left(45)

        self.assertEqual(error_message, 'Invalid user ID; should be a string')

    def test_decrement_followed_pairs_left_success(self):
        success1, error_message1 = self.mongo_followed_pairs_left_dao.insert_new_followed_pairs_left('1234', 5)
        success2, error_message2 = self.mongo_followed_pairs_left_dao.decrement_followed_pairs_left('1234')

        self.assertTrue(success1 and success2)

        num_pairs_available, error_message3 = self.mongo_followed_pairs_left_dao.get_followed_pairs_left('1234')

        self.assertEqual(num_pairs_available, 4)

    def test_decrement_zero_followed_pairs_left(self):
        success1, error_message1 = self.mongo_followed_pairs_left_dao.insert_new_followed_pairs_left('12345', 0)
        success2, error_message2 = self.mongo_followed_pairs_left_dao.decrement_followed_pairs_left('12345')

        self.assertTrue(success1 and success2)

        num_pairs_available, error_message3 = self.mongo_followed_pairs_left_dao.get_followed_pairs_left('12345')

        self.assertEqual(num_pairs_available, 0)

    def test_decrement_negative_followed_pairs_left(self):
        success1, error_message1 = self.mongo_followed_pairs_left_dao.insert_new_followed_pairs_left('8', -1)
        success2, error_message2 = self.mongo_followed_pairs_left_dao.decrement_followed_pairs_left('8')

        self.assertTrue(success1 and success2)

        num_pairs_available, error_message3 = self.mongo_followed_pairs_left_dao.get_followed_pairs_left('8')

        self.assertEqual(num_pairs_available, -1)

    def test_get_followed_pairs_left_user_id_fail(self):
        success, error_message = self.mongo_followed_pairs_left_dao.get_followed_pairs_left(45)

        self.assertEqual(error_message, 'Invalid user ID; should be a string')

    def test_get_followed_pairs_left_success(self):
        success1, error_message1 = self.mongo_followed_pairs_left_dao.insert_new_followed_pairs_left('9', 100)
        num_pairs_available, error_message = self.mongo_followed_pairs_left_dao.get_followed_pairs_left('9')

        self.assertEqual(num_pairs_available, 100)



if __name__ == '__main__':
    unittest.main()
