import sqlite3
import uuid
from Oanda.Config.config import Config


class SubscriptionDAO:
    def __init__(self):
        self.connection = None
        self.db_file_path = Config.get_db_file_path()

    """
        A private function that will create the subscriptions table -- WARNING: if the database already exists, this will
        drop it and recreate it
    """
    def _create_subscription_table(self):
        # Drop the user table if it already exists
        self._drop_subscription_table()

        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Create the table
        cursor.execute("""CREATE TABLE IF NOT EXISTS subscriptions (
                                 subscription_id text,
                                 user_id text,
                                 subscription_type text,
                                 monthly_cost real
                                 )""")

        self.connection.commit()
        self.connection.close()

    """
        A helper function for dropping the subscriptions table
    """
    def _drop_subscription_table(self):
        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Drop the user table if it already exists
        cursor.execute("""DROP TABLE IF EXISTS subscriptions""")

        self.connection.commit()
        self.connection.close()

    def _generate_subscription_id(self, user_id):
        return user_id + '-' + str(uuid.uuid1())

    def _check_subscription_parameters(self, user_id, subscription_type, subscription_cost):
        return isinstance(user_id, str) and isinstance(subscription_type, str) and isinstance(subscription_cost, float)

    def insert_new_subscription(self, user_id, subscription_type, subscription_cost):
        valid_parameters = self._check_subscription_parameters(user_id, subscription_type, subscription_cost)

        if not valid_parameters:
            return False, 'Invalid parameters used when trying to add a new subscription'

        new_subscription_id = self._generate_subscription_id(user_id)

        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO subscriptions VALUES ('{}', '{}', '{}', {})".format(new_subscription_id, user_id,
                                                                                          subscription_type,
                                                                                          subscription_cost))

        self.connection.commit()
        self.connection.close()

        return True, None

    def update_subscription(self, user_id, subscription_type, subscription_cost):
        valid_parameters = self._check_subscription_parameters(user_id, subscription_type, subscription_cost)

        if not valid_parameters:
            return False, 'Invalid parameters used when trying to update a subscription'

        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Get the user based on their first and last name
        cursor.execute("UPDATE subscriptions SET subscription_type = '{}', monthly_cost = {} WHERE user_id = '{}'"
                       .format(subscription_type, subscription_cost, user_id))

        self.connection.commit()
        self.connection.close()

        return True, None

    def get_monthly_bill(self, user_id):
        if not isinstance(user_id, str):
            return None, 'Invalid user ID; should be a string'

        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Get the user based on their first and last name
        cursor.execute("SELECT monthly_cost FROM subscriptions WHERE user_id = '{}'".format(user_id))
        monthly_bill = cursor.fetchone()

        self.connection.commit()
        self.connection.close()

        return monthly_bill, None
