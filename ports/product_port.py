# ports/product_port.py

from abc import ABC, abstractmethod

class ProductPort(ABC):

    @abstractmethod
    def add_product(self, product_data):
        pass

    @abstractmethod
    def get_all_products(self):
        pass
