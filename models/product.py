from infrastructure.db import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(120), nullable=True)
    stock = db.Column(db.Integer, nullable=False)
    order_products = db.relationship('OrderProduct', backref='product', lazy=True)
    reviews = db.relationship('Review', backref='product', lazy=True)
