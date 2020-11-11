import pymongo
from bson import ObjectId


"""
A class for accessing the user table in the database
"""


class MongoUserDAO:
    """
    The init function sets up a database connection object, a list of available subscriptions, and the user database
    file path
    """

    def __init__(self):
        mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')

        self.mongo_db = mongo_client['forex']

        self.users_collection = self.mongo_db['users']

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

    def _check_insert_new_user_parameters(self, username, first_name, last_name):
        # Check the parameter data types
        if not isinstance(username, str) or not isinstance(first_name, str) or not isinstance(last_name, str):
            return False

        # Make sure the parameters aren't empty
        if len(username) == 0 or len(first_name) == 0 or len(last_name) == 0:
            return False

        # Return True if all checks pass
        return True

    """
        A helper function for checking if username is already in use before creating a user

        Parameters:
            username (str): The username for the new user

        Returns:
            True if username already in use, False if username is not
        """

    def _check_user_exists(self, username):
        user = self.users_collection.find_one({'username': username})

        if user is None:
            return False
        else:
            return True

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

    def insert_new_user(self, username, first_name, last_name, password):
        # Make sure the parameters are valid
        valid_parameters = self._check_insert_new_user_parameters(username, first_name, last_name)

        # Return null plus an error message if the parameters are invalid
        if not valid_parameters:
            return None, 'Invalid new user parameters'

        if self._check_user_exists(username):
            return None, 'Username already in use'

        new_user = self.users_collection.insert_one({'username': username, 'first_name': first_name,
                                                     'last_name': last_name, 'password': password})

        # Return the user ID and a null error message
        return str(new_user.inserted_id), None

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

        # Return null plus an error message if the parameters are invalid
        if not valid_parameters:
            return None, 'Invalid get user by name parameters'

        user = self.users_collection.find({'first_name': first_name, 'last_name': last_name})

        # Return the user and a null error message
        return user, None

    """
    A function that returns a user with matching user_id

    Parameters: 
        user_id (str): the user_id to search the database for

    Returns:
        The user (null if the transaction was unsuccessful) and an error message (null if successful)
    """

    def get_user_by_userid(self, user_id):
        user = self.users_collection.find_one({'_id': ObjectId(user_id)})

        # Return the user and a null error message
        return user, None

    def login(self, username, password):
        user = self.users_collection.find_one({'username': username, 'password': password})

        if user is not None:
            return str(user['_id']), None

        else:
            return None, 'Invalid username and/or password'
