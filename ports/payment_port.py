from abc import ABC, abstractmethod

class PaymentPort(ABC):

    @abstractmethod
    def create_order(self, amount, currency):
        pass
