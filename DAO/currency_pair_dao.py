import sqlite3
import uuid

class CurrencyPairDAO:
    def __init__(self):
        self.connection = None

        self.db_file_path = 'C:/Users/Caleb-PC/PycharmProjects/ForexDataDownloader/Database/forex.db'

    """
        A private function that will create the pairs_followed table -- WARNING: if the database already exists, this will
        drop it and recreate it
    """

    def _create_currency_pairs_table(self):
        # Drop the user table if it already exists
        self._drop_currency_pairs_table()

        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Create the table
        cursor.execute("""CREATE TABLE IF NOT EXISTS currency_pairs (
                                     currency_id text,
                                     currency_name text
                                     )""")

        self.connection.commit()
        self.connection.close()

    """
        A helper function for dropping the pairs_followed table
    """

    def _drop_currency_pairs_table(self):
        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Drop the user table if it already exists
        cursor.execute("""DROP TABLE IF EXISTS currency_pairs""")

        self.connection.commit()
        self.connection.close()

    def _generate_currency_id(self, currencyName):
        return currencyName + '-' + str(uuid.uuid1())

    def add_currency_pair(self, currency_name):
        currency_id = self._generate_currency_id(currency_name)

        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Drop the user table if it already exists
        cursor.execute("INSERT INTO currency_pairs VALUES('{}','{}')".format(currency_id, currency_name))

        self.connection.commit()
        self.connection.close()

        return True, None

    def get_currency_pair(self, currency_id):
        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Drop the user table if it already exists
        cursor.execute("SELECT * FROM currency_pairs WHERE currency_id = ?", (currency_id,))
        result = cursor.fetchone()

        self.connection.commit()
        self.connection.close()

        return result, None

    def get_all_currency_pairs(self):
        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Drop the user table if it already exists
        cursor.execute("SELECT * FROM currency_pairs")
        result = cursor.fetchall()

        self.connection.commit()
        self.connection.close()

        return result, None

