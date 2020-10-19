import sqlite3
import uuid
from Oanda.Config.config import Config


class FollowedPairsLeftDAO:
    def __init__(self):
        self.connection = None
        self.db_file_path = Config.get_db_file_path()

    """
        A private function that will create the followed pairs left table -- WARNING: if the database already exists, this will
        drop it and recreate it
    """
    def _create_followed_pairs_left_table(self):
        # Drop the user table if it already exists
        self._drop_followed_pairs_left_table()

        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Create the table
        cursor.execute("""CREATE TABLE IF NOT EXISTS followed_pairs_left (
                                 followed_pairs_left_id text,
                                 user_id text,
                                 num_pairs_available integer
                                 )""")

        self.connection.commit()
        self.connection.close()

    """
        A helper function for dropping the followed pairs left table
    """
    def _drop_followed_pairs_left_table(self):
        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Drop the user table if it already exists
        cursor.execute("""DROP TABLE IF EXISTS followed_pairs_left""")

        self.connection.commit()
        self.connection.close()

    def _generate_followed_pairs_left_id(self, user_id):
        return user_id + '-' + str(uuid.uuid1())

    def _check_followed_pairs_left_parameters(self, user_id, num_pairs_available):
        return isinstance(user_id, str) and isinstance(num_pairs_available, int)

    def insert_new_followed_pairs_left(self, user_id, num_pairs_available):
        valid_parameters = self._check_followed_pairs_left_parameters(user_id, num_pairs_available)

        if not valid_parameters:
            return False, 'Invalid parameters used when trying to add a new followed pairs left'

        new_followed_pairs_left_id = self._generate_followed_pairs_left_id(user_id)

        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO followed_pairs_left VALUES ('{}', '{}', {})".format(new_followed_pairs_left_id,
                                                                                        user_id, num_pairs_available))

        self.connection.commit()
        self.connection.close()

        return True, None

    def update_followed_pairs_left(self, user_id, num_pairs_available):
        valid_parameters = self._check_followed_pairs_left_parameters(user_id, num_pairs_available)

        if not valid_parameters:
            return False, 'Invalid parameters used when trying to update a followed pairs left'

        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Get the user based on their first and last name
        cursor.execute("UPDATE followed_pairs_left SET num_pairs_available = {} WHERE user_id = '{}'"
                       .format(num_pairs_available, user_id))

        self.connection.commit()
        self.connection.close()

        return True, None

    def decrement_followed_pairs_left(self, user_id):
        if not isinstance(user_id, str):
            return False, 'Invalid user ID; should be a string'

        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Get the user based on their first and last name
        cursor.execute("UPDATE followed_pairs_left SET num_pairs_available = num_pairs_available - 1 WHERE user_id = '{}' AND num_pairs_available > 0"
                       .format(user_id))

        self.connection.commit()
        self.connection.close()

        return True, None

    def get_followed_pairs_left(self, user_id):
        if not isinstance(user_id, str):
            return None, 'Invalid user ID; should be a string'

        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Get the user based on their first and last name
        cursor.execute("SELECT num_pairs_available FROM followed_pairs_left WHERE user_id = '{}'".format(user_id))
        num_pairs_available = cursor.fetchone()

        self.connection.commit()
        self.connection.close()

        return num_pairs_available, None
