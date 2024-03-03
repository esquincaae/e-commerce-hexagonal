from . import db

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=True)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(120), nullable=False)
    order_products = db.relationship('OrderProduct', backref='order', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'seller_id': self.seller_id,
            'amount': self.amount,
            'status': self.status,
            'order_products': [order_product.to_dict() for order_product in self.order_products]
        }