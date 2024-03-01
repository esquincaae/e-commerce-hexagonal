class UserService:
    def __init__(self, user_adapter):
        self.user_adapter = user_adapter

    def create_user(self, user_data):
        return self.user_adapter.add_user(user_data)

    def authenticate_user(self, credentials):
        return self.user_adapter.authenticate_user(credentials)
