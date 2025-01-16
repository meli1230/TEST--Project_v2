import unittest
import threading
from unittest.mock import patch
from data.storage import users
from models.user import User
from services.user_service import UserService

class TestListUserIncompleteData(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()
        users.clear()
        users.append(User(1, "John Doe", ""))  # Fus orar gol.

    def test_list_user_with_empty_timezone(self):
        """Test care eșuează dacă aplicația nu gestionează fusul orar gol."""
        with patch("builtins.print") as mock_print:
            self.user_service.list_users()
            mock_print.assert_any_call("ID: 1, Name: John Doe, Timezone: [Invalid]")