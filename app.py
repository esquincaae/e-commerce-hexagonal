from flask import Flask, jsonify, request
import logging
from domain_logic.user_service import UserService
from domain_logic.product_service import ProductService
from domain_logic.order_service import OrderService
from domain_logic.security_service import SecurityService
from adapters.sqlalchemy_user_adapter import SQLAlchemyUserAdapter
from adapters.sqlalchemy_product_adapter import SQLAlchemyProductAdapter
from adapters.sqlalchemy_order_adapter import SQLAlchemyOrderAdapter
from adapters.paypal_adapter import PayPalAdapter
from infrastructure.db import db, init_app
import config

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(config.Config)

# Inicialización de la base de datos y los servicios
init_app(app)
security_service = SecurityService(app)
user_adapter = SQLAlchemyUserAdapter(app)
product_adapter = SQLAlchemyProductAdapter()
order_adapter = SQLAlchemyOrderAdapter()
paypal_adapter = PayPalAdapter(app.config['PAYPAL_CLIENT_ID'], app.config['PAYPAL_CLIENT_SECRET'])

user_service = UserService(user_adapter, security_service)
product_service = ProductService(product_adapter)
order_service = OrderService(order_adapter)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()
    user = user_service.create_user(user_data)
    return jsonify(user), 201

@app.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()
    user = user_service.authenticate_user(user_data)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/products', methods=['GET'])
def list_products():
    products = product_service.get_all_products()
    return jsonify([product.to_dict() for product in products])

@app.route('/orders', methods=['POST'])
def create_order():
    order_data = request.get_json()
    order = order_service.create_order(order_data)
    return jsonify(order), 201

@app.route('/create-paypal-order', methods=['POST'])
def create_paypal_order():
    data = request.get_json()
    order_id = paypal_adapter.create_order(data['amount'], data.get('currency', 'USD'))
    if order_id:
        return jsonify({'order_id': order_id}), 200
    else:
        logger.error('Error creating PayPal order')
        return jsonify({'error': 'There was an error creating the PayPal order'}), 500

# Manejo global de errores
@app.errorhandler(Exception)
def handle_exception(error):
    logger.error(f'Unexpected error: {error}')
    return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
