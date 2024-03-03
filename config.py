import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'f47bcf05d245e6bcb13f908c3f92dc6f0ac788cfff7c4f38')
    PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID', 'Acf2jPhS1KA0Kfp9WzeeGYbQot_exWfRvQUAjhcNzygCGbsAbNCKSDDtM0z1JbYpwbllHLbdZuqe3gMX')
    PAYPAL_CLIENT_SECRET = os.getenv('PAYPAL_CLIENT_SECRET', 'EDtVXB0ynpOUcUmfHbZcABOnQ_Lf8WLx-V-KE-RuVlv-Y5m6bNdHRCAZUkf1R5pzo-LrCQWN5tsVDfbz')
