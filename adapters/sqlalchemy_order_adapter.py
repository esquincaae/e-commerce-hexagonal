from ports.order_port import OrderPort
from models import db, Order, OrderProduct

class SQLAlchemyOrderAdapter(OrderPort):

    def add_order(self, order_data, products):
        new_order = Order(**order_data)
        db.session.add(new_order)
        db.session.commit()

        for product_id in products:
            order_product = OrderProduct(product_id=product_id, order_id=new_order.id)
            db.session.add(order_product)
        db.session.commit()
        return new_order

    def update_order(self, order_id, status):
        order = Order.query.get(order_id)
        order.status = status
        db.session.commit()
        return order

    def get_orders_by_user(self, user_id):
        return Order.query.filter_by(customer_id=user_id).all()
