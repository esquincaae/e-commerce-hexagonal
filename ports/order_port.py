# ports/order_port.py

from abc import ABC, abstractmethod

class OrderPort(ABC):

    @abstractmethod
    def add_order(self, order_data, products):
        pass

    @abstractmethod
    def update_order(self, order_id, status):
        pass

    @abstractmethod
    def get_orders_by_user(self, user_id):
        pass
