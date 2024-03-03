from . import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(120), nullable=True)
    stock = db.Column(db.Integer, nullable=True)
    order_products = db.relationship('OrderProduct', backref='product', lazy=True)
    reviews = db.relationship('Review', backref='product', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'seller_id': self.seller_id,
            'price': self.price,
            'category': self.category,
            'stock': self.stock,
            'order_products': self.order_products
        }