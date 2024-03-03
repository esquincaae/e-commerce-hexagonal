from ports.order_port import OrderPort
from models import db, Order, OrderProduct

class SQLAlchemyOrderAdapter(OrderPort):

    def add_order(self, order_data, products):
        order2 = order_data
        order_data.pop("order_products", None)
        new_order = Order(**order2)
        db.session.add(order_data)
        print("se añadio a la db")
        db.session.commit()
        for id in products:
            print("si entra")
            order_product = OrderProduct(product_id=id, order_id=new_order.id)
            db.session.add(order_product)
        print("ya salio")
        db.session.commit()
        print("ya se fue")
        return order_data

    def update_order(self, order_id, status):
        order = Order.query.get(order_id)
        order.status = status
        db.session.commit()
        return order

    def get_orders_by_user(self, user_id):
        return Order.query.filter_by(customer_id=user_id).all()
