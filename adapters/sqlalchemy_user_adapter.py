# adapters/sqlalchemy_user_adapter.py

from ports.user_port import UserPort
from models import db, User
from flask_bcrypt import Bcrypt

class SQLAlchemyUserAdapter(UserPort):

    def __init__(self, app):
        self.bcrypt = Bcrypt(app)

    def add_user(self, user_data):
        user_data['password'] = self.bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()
        return user

    def authenticate_user(self, email, password):
        user = User.query.filter_by(email=email).first()
        if user and self.bcrypt.check_password_hash(user.password, password):
            return user
        return None
