# adapters/paypal_adapter.py

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCreateRequest
from ports.payment_port import PaymentPort

class PayPalAdapter(PaymentPort):

    def __init__(self, client_id, client_secret):
        self.environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
        self.client = PayPalHttpClient(self.environment)

    def create_order(self, amount, currency='USD'):
        request = OrdersCreateRequest()
        request.prefer('return=representation')
        request.request_body({
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": currency,
                        "value": amount
                    }
                }
            ]
        })

        try:
            response = self.client.execute(request)
            return response.result.id
        except IOError as ioe:
            # Manejo de errores
            print(ioe)
            return None
