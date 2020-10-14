import sqlite3
import uuid

class PairsFollowedDAO:
    def __init__(self):
        self.connection = None

        self.db_file_path = 'C:/Users/Caleb-PC/PycharmProjects/ForexDataDownloader/Database/forex.db'

    """
        A private function that will create the pairs_followed table -- WARNING: if the database already exists, this will
        drop it and recreate it
    """
    def _create_pairs_followed_table(self):
        # Drop the user table if it already exists
        self._drop_pairs_followed_table()

        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Create the table
        cursor.execute("""CREATE TABLE IF NOT EXISTS pairs_followed (
                                 pair_followed_id text,
                                 user_id text,
                                 currency_id text
                                 )""")

        self.connection.commit()
        self.connection.close()

    """
        A helper function for dropping the pairs_followed table
    """
    def _drop_pairs_followed_table(self):
        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Drop the user table if it already exists
        cursor.execute("""DROP TABLE IF EXISTS pairs_followed""")

        self.connection.commit()
        self.connection.close()

    def _generate_pair_followed_id(self, currency_id, user_id):
        return currency_id + '-' + str(uuid.uuid1()) + '-' + user_id

    def insert_new_pair_followed(self, user_id, currency_id):
        new_pair_followed_id = self._generate_pair_followed_id(currency_id, user_id)

        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO pairs_followed VALUES ('{}', '{}', '{}')".format(new_pair_followed_id, user_id, currency_id))

        self.connection.commit()
        self.connection.close()

        return True, None

    def get_pairs_followed(self, user_id):
        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Get the user based on their first and last name
        cursor.execute("SELECT * FROM pairs_followed WHERE user_id = ?", (user_id,))
        pairs_followed = cursor.fetchall()

        self.connection.commit()
        self.connection.close()

        return pairs_followed, None

    # TODO: Not sure if we want this as a seperate function or done simultaneously with getting followed pairs
    def get_num_pairs_followed(self, user_id):
        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Get the user based on their first and last name
        cursor.execute("SELECT COUNT(*) FROM pairs_followed WHERE user_id = ?", (user_id,))
        num_pairs_followed = cursor.fetchall()

        self.connection.commit()
        self.connection.close()

        return num_pairs_followed, None




