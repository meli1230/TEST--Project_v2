import unittest
from unittest.mock import patch
from data.storage import users
from models.user import User
from services.user_service import UserService


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.service = UserService()
        users.clear()  # Curățăm lista de utilizatori înainte de fiecare test

    @patch('builtins.input', side_effect=['John Doe', '1'])
    def test_add_user_with_duplicate_name(self, mock_input):
        """Test adding a user with a duplicate name."""
        users.append(User(1, 'John Doe', 'UTC')) # Adăugăm un utilizator existent cu numele 'John Doe'
        self.service.add_user()  #Adăugăm un al doilea utilizator cu același nume
        self.assertEqual(len(users), 1)  #Ar trebui sa se adauge doar un user, dar se adauga 2