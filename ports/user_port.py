# ports/user_port.py

from abc import ABC, abstractmethod

class UserPort(ABC):

    @abstractmethod
    def add_user(self, user_data):
        pass

    @abstractmethod
    def authenticate_user(self, email, password):
        pass
