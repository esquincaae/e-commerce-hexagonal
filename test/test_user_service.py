import unittest
from domain_logic.user_service import UserService
from unittest.mock import MagicMock

class TestUserService(unittest.TestCase):
    def test_create_user(self):
        user_adapter = MagicMock()
        security_service = MagicMock()
        user_service = UserService(user_adapter, security_service)

        user_service.create_user({'name': 'Test', 'password': 'password'})
        security_service.generate_password_hash.assert_called_once()
