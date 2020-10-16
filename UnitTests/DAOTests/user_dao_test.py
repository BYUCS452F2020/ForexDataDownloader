import unittest
from DAO.user_dao import UserDAO


# TODO: add more tests for failures, etc.
class UserDaoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.user_dao = UserDAO()

    def test_insert_new_user_username_fail(self):
        self.user_dao._create_user_table()

        user_id, error_message = self.user_dao.insert_new_user('', 'Billy', 'Bob', 'password')

        self.assertEqual(error_message, 'Invalid new user parameters')

    def test_insert_new_user_name_fail(self):
        self.user_dao._create_user_table()

        user_id, error_message = self.user_dao.insert_new_user('billybob123', 'Billy', '', 'password')

        self.assertEqual(error_message, 'Invalid new user parameters')

    def test_insert_new_user_success(self):
        self.user_dao._create_user_table()

        user_id, error_message = self.user_dao.insert_new_user('billybob123', 'Billy', 'Bob', 'password')

        self.assertIsNotNone(user_id)

    def test_get_user_by_name_success(self):
        self.user_dao._create_user_table()

        user_id, error_message = self.user_dao.insert_new_user('billybob123', 'Billy', 'Bob', 'password')
        user, error_message = self.user_dao.get_user_by_name('Billy', 'Bob')

        self.assertIsNotNone(user)

    def test_create_user_already_exists_fail(self):
        self.user_dao._create_user_table()

        self.user_dao.insert_new_user('billybob123', 'Billy', 'Bob', 'password')
        user_id, error_message = self.user_dao.insert_new_user('billybob123', 'Bill', 'Bob', 'password')

        self.assertEqual(error_message, 'Username already in use')

    def test_change_user_id(self):
        self.user_dao._create_user_table()

        self.user_dao.insert_new_user('billybob123', 'Billy', 'Bob', 'password')
        self.user_dao._change_user_id('billybob123', '123')
        user, error_message = self.user_dao.get_user_by_name('Billy', 'Bob')

        self.assertIsNotNone(user)

    def test_get_user_by_user_id(self):
        self.user_dao._create_user_table()

        self.user_dao.insert_new_user('billybob123', 'Billy', 'Bob', 'password')
        self.user_dao._change_user_id('billybob123', '123')
        user, error_message = self.user_dao.get_user_by_userid('123')

        self.assertIsNotNone(user)

    def test_login_username_fail(self):
        self.user_dao._create_user_table()

        self.user_dao.insert_new_user('billybob123', 'Billy', 'Bob', 'crappy_password')
        user_id, error_message = self.user_dao.login('billybob12', 'crappy_password')

        self.assertIsNone(user_id)

    def test_login_password_fail(self):
        self.user_dao._create_user_table()

        self.user_dao.insert_new_user('billybob123', 'Billy', 'Bob', 'crappy_password')
        user_id, error_message = self.user_dao.login('billybob123', 'crappy_passwrd')

        self.assertIsNone(user_id)

    def test_login_success(self):
        self.user_dao._create_user_table()

        self.user_dao.insert_new_user('billybob123', 'Billy', 'Bob', 'crappy_password')
        user_id, error_message = self.user_dao.login('billybob123', 'crappy_password')

        self.assertIsNotNone(user_id)
        self.assertTrue('billybob123' in user_id[0])


if __name__ == '__main__':
    unittest.main()
