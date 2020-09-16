import sqlite3
import uuid


# TODO: create more methods that we need
# TODO: add checks to make sure we don't create a user with a username that already exists, etc.
# TODO: add more user parameters that we need
"""Class for accessing the user table in the database"""
class UserDao:
    """
    The init function sets up a database connection object, a list of available subscriptions, and the user database
    file path
    """
    def __init__(self):
        # Database connection object
        self.connection = None

        # A list of available subscription types
        self.available_subscription_types = ['basic', 'advanced']

        # CHANGE THIS FILE PATH TO WHEREVER THE DB FILE IS LOCATED ON YOUR COMPUTER
        self.db_file_path = '/Users/mymac/Google_Drive/CS/CS452/ForexDataDownloader/ForexDataDownloader/Database/forex.db'

    """
    A private function that will create the user table -- WARNING: if the database already exists, this will
    drop it and recreate it
    """
    def _create_user_table(self):
        # Drop the user table if it already exists
        self._drop_user_table()

        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Create the table
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

    """
    A helper function for dropping the user table
    """
    def _drop_user_table(self):
        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Drop the user table if it already exists
        cursor.execute("""DROP TABLE IF EXISTS users""")

        self.connection.commit()
        self.connection.close()

    """
    A helper function for checking the parameters passed in when trying to insert a new user into the user table
    
    Parameters:
        username (str): The username for the new user
        first_name (str): The first name of the new user
        last_name (str): The last name of the new user
        email (str): The email of the new user
        subscription_type (str): The type of subscription that the new user wants to have
        
    Returns:
        A boolean indicating whether the parameters are valid
    """
    def _check_insert_new_user_parameters(self, username, first_name, last_name, email, subscription_type):
        # Check the parameter data types
        if not isinstance(username, str) or not isinstance(first_name, str) or not isinstance(last_name, str) or not \
                isinstance(email, str) or not isinstance(subscription_type, str):
            return False

        # Make sure the parameters aren't empty
        if len(username) == 0 or len(first_name) == 0 or len(last_name) == 0 or len(email) == 0 or len(subscription_type) == 0:
            return False

        # Make sure the subscription type is valid
        if subscription_type not in self.available_subscription_types:
            return False

        # Return True if all checks pass
        return True

    """
    A helper function for generating a unique user ID for a new user
    
    Parameters:
        username (str): The username for the new user
        first_name (str): The first name of the new user
        last_name (str): The last name of the new user
        
    Returns:
        A unique user ID (a string)
    """
    def _generate_user_id(self, username, first_name, last_name):
        # Use the first name, last name, and username, along with the UUID module, to create a unique user ID
        return first_name + '-' + username + '-' + str(uuid.uuid1()) + '-' + last_name

    """
    A function for creating a new user in the user table
    
    Parameters:
        username (str): The username for the new user
        first_name (str): The first name of the new user
        last_name (str): The last name of the new user
        email (str): The email of the new user
        subscription_type (str): The type of subscription that the new user wants to have
        
    Returns:
        A boolean indicating if the insertion was successful and an error message (null if successful)
    """
    def insert_new_user(self, username, first_name, last_name, email, subscription_type):
        # Make sure the parameters are valid
        valid_parameters = self._check_insert_new_user_parameters(username, first_name, last_name, email, subscription_type)

        # Return False plus an error message if the parameters are invalid
        if not valid_parameters:
            return False, 'Invalid new user parameters'

        # Generate a new user ID
        new_user_id = self._generate_user_id(username, first_name, last_name)

        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Insert the new user into the user table
        cursor.execute("INSERT INTO users VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {})".format(new_user_id, username,
                                                                                                  first_name, last_name,
                                                                                                  email,
                                                                                                  subscription_type, 1))

        self.connection.commit()
        self.connection.close()

        # Return True and a null error message
        return True, None

    """
    A helper function for checking the parameters passed in when trying to get user based on their first and last name
    
    Parameters:
        first_name (str): The first name of the user
        last_name (str): The last name of the user
        
    Returns:
        A boolean indicating whether the parameters are valid
    """
    def _check_get_user_by_name_parameters(self, first_name, last_name):
        # Check the parameter data types
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            return False

        # Make sure the parameters aren't empty
        if len(first_name) == 0 or len(last_name) == 0:
            return False

        # Return True if all checks pass
        return True

    """
    A function for retrieving a user based on their first and last name
    
    Parameters:
        first_name (str): The first name of the user
        last_name (str): The last name of the user
        
    Returns:
        The user (null if the transaction was unsuccessful) and an error message (null if successful)
    """
    def get_user_by_name(self, first_name, last_name):
        # Make sure the parameters are valid
        valid_parameters = self._check_get_user_by_name_parameters(first_name, last_name)

        # Return False plus an error message if the parameters are invalid
        if not valid_parameters:
            return None, 'Invalid get user by name parameters'

        # Connect to the database
        self.connection = sqlite3.connect(self.db_file_path)
        cursor = self.connection.cursor()

        # Get the user based on their first and last name
        cursor.execute("SELECT * FROM users WHERE first_name = '{}' AND last_name = '{}'".format(first_name, last_name))
        user = cursor.fetchone()

        self.connection.commit()
        self.connection.close()

        # Return the user and a null error message
        return user, None