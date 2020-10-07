import unittest
from DAO.user_dao import UserDao

# TODO: add more tests for failures, etc.
class UserDaoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.user_dao = UserDao()

    def test_insert_new_user_username_fail(self):
        self.user_dao._create_user_table()

        success, error_message = self.user_dao.insert_new_user('', 'Billy', 'Bob', 'bob@gmail.com', 'basic')

        self.assertEqual(error_message, 'Invalid new user parameters')

    def test_insert_new_user_name_fail(self):
        self.user_dao._create_user_table()

        success, error_message = self.user_dao.insert_new_user('billybob123', 'Billy', '', 'bob@gmail.com', 'basic')

        self.assertEqual(error_message, 'Invalid new user parameters')

    def test_insert_new_user_email_fail(self):
        self.user_dao._create_user_table()

        success, error_message = self.user_dao.insert_new_user('billybob123', 'Billy', 'Bob', '', 'basic')

        self.assertEqual(error_message, 'Invalid new user parameters')

    def test_insert_new_user_subscription_type_fail(self):
        self.user_dao._create_user_table()

        success, error_message = self.user_dao.insert_new_user('billybob123', 'Billy', 'Bob', '', 'basicc')

        self.assertEqual(error_message, 'Invalid new user parameters')

    def test_insert_new_user_success(self):
        self.user_dao._create_user_table()

        success, error_message = self.user_dao.insert_new_user('billybob123', 'Billy', 'Bob', 'bob@gmail.com', 'basic')

        self.assertTrue(success)

    def test_get_user_by_name_success(self):
        self.user_dao._create_user_table()

        success, error_message = self.user_dao.insert_new_user('billybob123', 'Billy', 'Bob', 'bob@gmail.com', 'basic')
        user, error_message = self.user_dao.get_user_by_name('Billy', 'Bob')

        self.assertIsNotNone(user)


if __name__ == '__main__':
    unittest.main()
