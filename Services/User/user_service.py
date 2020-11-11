from MongoDAO.mongo_user_dao import MongoUserDAO


# TODO: add docs
class UserService:
    def __init__(self):
        self.user_dao = MongoUserDAO()

    def create_user(self, username, first_name, last_name, password):
        return self.user_dao.insert_new_user(username, first_name, last_name, password)

    def login(self, username, password):
        return self.user_dao.login(username, password)
