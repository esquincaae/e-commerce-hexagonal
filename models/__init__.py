from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .user import User 
from .review import Review
from .product import Product
from .order import Order
from .order_product import OrderProduct