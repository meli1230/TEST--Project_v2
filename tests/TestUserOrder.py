import unittest
import threading
from unittest.mock import patch
from data.storage import users
from models.user import User
from services.user_service import UserService

class TestUserOrder(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()
        users.clear()
        users.append(User(2, "Jane Doe", "UTC"))
        users.append(User(1, "John Doe", "UTC"))

    def test_user_order(self):
        """Test care eșuează dacă utilizatorii nu sunt listați în ordinea ID-urilor."""
        sorted_users = sorted(users, key=lambda u: u.user_id)
        self.assertEqual(users, sorted_users,
                         "Utilizatorii nu sunt listați în ordinea ID-urilor.")