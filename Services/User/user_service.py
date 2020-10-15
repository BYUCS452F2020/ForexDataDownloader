# TODO: get imports once the needed modules are implemented
from DAO.user_dao import UserDAO

# TODO: add docs once service is implemented
class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    # TODO: implement and add docs when user dao is implemented
    def create_user(self, username, first_name, last_name, password):
        if self.user_dao.insert_new_user(username, first_name, last_name, password):
            pass
        else:
            pass

    # TODO: implement and add docs when user dao is implemented
    def login(self, username, password):
        pass
