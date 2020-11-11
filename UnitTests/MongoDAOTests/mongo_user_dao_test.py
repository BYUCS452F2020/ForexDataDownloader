import unittest
from MongoDAO.mongo_user_dao import MongoUserDAO


# TODO: add more tests for failures, etc.
class MongoUserDaoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mongo_user_dao = MongoUserDAO()

    def test_insert_new_user_username_fail(self):
        user_id, error_message = self.mongo_user_dao.insert_new_user('', 'Billy', 'Bob', 'password')

        self.assertEqual(error_message, 'Invalid new user parameters')

    def test_insert_new_user_name_fail(self):
        user_id, error_message = self.mongo_user_dao.insert_new_user('billybob123', 'Billy', '', 'password')

        self.assertEqual(error_message, 'Invalid new user parameters')

    def test_insert_new_user_success(self):
        user_id, error_message = self.mongo_user_dao.insert_new_user('billybob123', 'Billy', 'Bob', 'password')

        self.assertIsNotNone(user_id)

    def test_get_user_by_name_success(self):
        user, error_message = self.mongo_user_dao.get_user_by_name('Billy', 'Bob')

        self.assertIsNotNone(user)

    def test_create_user_already_exists_fail(self):
        user_id, error_message = self.mongo_user_dao.insert_new_user('billybob123', 'Bill', 'Bob', 'password')

        self.assertEqual(error_message, 'Username already in use')

    def test_get_user_by_user_id(self):
        user_id, error_message = self.mongo_user_dao.login('billybob123', 'password')
        user, error_message = self.mongo_user_dao.get_user_by_userid(user_id)

        self.assertIsNotNone(user)

    def test_login_username_fail(self):
        user_id, error_message = self.mongo_user_dao.login('billybob123', 'crappy_password')

        self.assertIsNone(user_id)

    def test_login_password_fail(self):
        user_id, error_message = self.mongo_user_dao.login('billybob123', 'crappy_passwrd')

        self.assertIsNone(user_id)

    def test_login_success(self):
        user_id, error_message = self.mongo_user_dao.login('billybob123', 'password')

        self.assertIsNotNone(user_id)


if __name__ == '__main__':
    unittest.main()
