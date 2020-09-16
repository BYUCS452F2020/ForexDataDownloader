import sqlite3
import uuid


# TODO: create more methods that we need
# TODO: add more user parameters that we need
class UserDao:
    def __init__(self):
        self.connection = None
        self.available_subscription_types = ['basic', 'advanced']
        # CHANGE THIS FILE PATH TO WHEREVER THE DB FILE IS LOCATED ON YOUR COMPUTER
        self.db_file_path = '/Users/mymac/Google_Drive/CS/CS452/ForexDataDownloader/ForexDataDownloader/Database/users.db'

    def _create_user_table(self):
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        cursor.execute("""DROP TABLE IF EXISTS users""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                         user_id text,
                         username text,
                         first_name text,
                         last_name text,
                         email text,
                         subscription_type text,
                         reset_available integer
                         )""")

        self.connection.commit()
        self.connection.close()

    def _check_insert_new_user_parameters(self, username, first_name, last_name, email, subscription_type):
        if not isinstance(username, str) or not isinstance(first_name, str) or not isinstance(last_name, str) or not \
                isinstance(email, str) or not isinstance(subscription_type, str):
            return False

        if len(username) == 0 or len(first_name) == 0 or len(last_name) == 0 or len(email) == 0 or len(subscription_type) == 0:
            return False

        if subscription_type not in self.available_subscription_types:
            return False

        return True

    def _generate_user_id(self, first_name, last_name):
        return first_name + '-' + str(uuid.uuid1()) + '-' + last_name

    def insert_new_user(self, username, first_name, last_name, email, subscription_type):
        valid_parameters = self._check_insert_new_user_parameters(username, first_name, last_name, email, subscription_type)

        if not valid_parameters:
            return False, 'Invalid new user parameters'

        new_user_id = self._generate_user_id(first_name, last_name)

        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO users VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {})".format(new_user_id, username,
                                                                                                  first_name, last_name,
                                                                                                  email,
                                                                                                  subscription_type, 1))

        self.connection.commit()
        self.connection.close()

        return True, None

    def _check_get_user_by_name_parameters(self, first_name, last_name):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            return False

        if len(first_name) == 0 or len(last_name) == 0:
            return False

        return True

    def get_user_by_name(self, first_name, last_name):
        valid_parameters = self._check_get_user_by_name_parameters(first_name, last_name)

        if not valid_parameters:
            return None, 'Invalid get user by name parameters'

        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM users WHERE first_name = '{}' AND last_name = '{}'".format(first_name, last_name))
        user = cursor.fetchone()

        self.connection.commit()
        self.connection.close()

        return user, None
