class ProductService:
    def __init__(self, product_adapter):
        self.product_adapter = product_adapter

    def add_product(self, product_data):
        return self.product_adapter.add_product(product_data)

    def get_all_products(self):
        return self.product_adapter.get_all_products()
