from ports.product_port import ProductPort
from models import db, Product

class SQLAlchemyProductAdapter(ProductPort):

    def add_product(self, product_data):
        new_product = Product(**product_data)
        db.session.add(new_product)
        db.session.commit()
        return new_product

    def get_all_products(self):
        return Product.query.all()
