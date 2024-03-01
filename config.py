import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID', 'default_client_id')
    CLIENT_SECRET = os.getenv('PAYPAL_CLIENT_SECRET', 'default_client_secret')
