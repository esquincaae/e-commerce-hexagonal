from infrastructure.db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    products = db.relationship('Product', backref='seller', lazy=True)
    customer_orders = db.relationship('Order', foreign_keys='Order.customer_id',
                                      backref='customer', lazy=True)
    seller_orders = db.relationship('Order', foreign_keys='Order.seller_id',
                                    backref='seller', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)
