import unittest
from unittest.mock import patch
from data.storage import users, TIMEZONES
from services.user_service import UserService


class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()
        users.clear()

    @patch("builtins.input", side_effect=["", "1"])  # Nume gol, dar fus orar valid.
    def test_add_user_fails_with_empty_name(self, mock_input):
        self.user_service.add_user()
        self.assertEqual(len(users), 0, "Utilizatorul nu ar trebui să fie adăugat fără un nume valid.")

    @patch("builtins.input", side_effect=["Test User", "99"])  # Fus orar invalid.
    def test_add_user_defaults_to_utc_with_invalid_timezone(self, mock_input):
        self.user_service.add_user()
        self.assertEqual(users[0].timezone, "UTC", "Fusul orar ar trebui să fie UTC dacă input-ul este invalid.")