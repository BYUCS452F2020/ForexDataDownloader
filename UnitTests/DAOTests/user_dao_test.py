import unittest
from DAO.user_dao import UserDao


# TODO: add more tests for failures, etc.
class UserDaoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.user_dao = UserDao()

    def test_insert_new_user_name_fail(self):
        success, error_message = self.user_dao.insert_new_user('Billy', '', 'bob@gmail.com', 'basic')

        self.assertEqual(error_message, 'Invalid new user parameters')

    def test_insert_new_user_email_fail(self):
        success, error_message = self.user_dao.insert_new_user('Billy', 'Bob', '', 'basic')

        self.assertEqual(error_message, 'Invalid new user parameters')

    def test_insert_new_user_subscription_type_fail(self):
        success, error_message = self.user_dao.insert_new_user('Billy', 'Bob', '', 'basicc')

        self.assertEqual(error_message, 'Invalid new user parameters')

    def test_insert_new_user_success(self):
        success, error_message = self.user_dao.insert_new_user('Billy', 'Bob', 'bob@gmail.com', 'basic')

        self.assertTrue(success)

    def test_get_user_by_name_success(self):
        user, error_message = self.user_dao.get_user_by_name('Billy', 'Bob')

        self.assertIsNotNone(user)


if __name__ == '__main__':
    unittest.main()
