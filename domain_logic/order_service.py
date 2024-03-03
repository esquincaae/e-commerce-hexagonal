class OrderService:
    def __init__(self, order_adapter):
        self.order_adapter = order_adapter

    def create_order(self, order_data, products):
        print("create_order en order_service.py")
        return self.order_adapter.add_order(order_data, products)

    def get_orders_by_user(self, user_id):
        return self.order_adapter.get_orders_by_user(user_id)
