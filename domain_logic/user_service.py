from . import security_service

class UserService:
    def __init__(self, user_adapter, security_service):
        self.user_adapter = user_adapter

    def create_user(self, user_data):
        return self.user_adapter.add_user(user_data)

    def authenticate_user(self, credentials):
        return self.user_adapter.authenticate_user(credentials)
