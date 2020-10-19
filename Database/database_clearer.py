import sqlite3
from Oanda.Config.config import Config


class DatabaseClearer(object):

    @staticmethod
    def clear_database():
        # Connect to the database
        connection = sqlite3.connect(Config.get_db_file_path())
        cursor = connection.cursor()

        # Drop all the tables (except the currency pair table since it never changes)
        cursor.execute("""DROP TABLE IF EXISTS followed_pairs_left""")
        cursor.execute("""DROP TABLE IF EXISTS pairs_followed""")
        cursor.execute("""DROP TABLE IF EXISTS subscriptions""")
        cursor.execute("""DROP TABLE IF EXISTS users""")

        # Recreate the dropped tables
        cursor.execute("""CREATE TABLE IF NOT EXISTS followed_pairs_left (
                                 followed_pairs_left_id text,
                                 user_id text,
                                 num_pairs_available integer
                                 )""")
        # Create the table
        cursor.execute("""CREATE TABLE IF NOT EXISTS pairs_followed (
                                 pair_followed_id text,
                                 user_id text,
                                 currency_name text
                                 )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS subscriptions (
                                 subscription_id text,
                                 user_id text,
                                 subscription_type text,
                                 monthly_cost real
                                 )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                         user_id text,
                         username text,
                         first_name text,
                         last_name text,
                         password text
                         )""")

        # Execute
        connection.commit()
        connection.close()
