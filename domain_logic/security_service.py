from flask_bcrypt import Bcrypt

class SecurityService:
    def __init__(self, app=None):
        if app is not None:
            self.bcrypt = Bcrypt()
        else:
            self.bcrypt = Bcrypt(app)

    def set_app(self, app):
        self.bcrypt.init_app(app)

    def generate_password_hash(self, password):
        return self.bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password_hash(self, password_hash, password):
        return self.bcrypt.check_password_hash(password_hash, password)
