# tests/user_service_test.py
import unittest
from unittest.mock import patch
from data.storage import users
from services.user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        """Pregătește mediul de test."""
        self.service = UserService()  # Instanțiază serviciul fără baza de date
        users.clear()  # Golește lista globală

    @patch('builtins.input', side_effect=['Test User', '1'])
    def test_add_user_valid(self, mock_input):
        """Testează adăugarea unui utilizator valid."""
        self.service.add_user(1, 'Test User', 'UTC')  # Adaugă utilizatorul
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]['name'], 'Test User')
        self.assertEqual(users[0]['timezone'], 'UTC')

    def test_delete_user_valid(self):
        """Testează ștergerea unui utilizator."""
        self.service.add_user(1, 'Test User', 'UTC')  # Adaugă un utilizator
        self.service.delete_user('Test User')  # Șterge utilizatorul
        self.assertEqual(len(users), 0)

    def test_list_users_empty(self):
        """Testează listarea când nu există utilizatori."""
        with patch('builtins.print') as mock_print:
            self.service.list_users()
            mock_print.assert_any_call("No users found.")

    def test_list_users_with_data(self):
        """Testează listarea utilizatorilor existenți."""
        self.service.add_user(1, 'User One', 'UTC')
        self.service.add_user(2, 'User Two', 'Europe/London')
        with patch('builtins.print') as mock_print:
            self.service.list_users()
            mock_print.assert_any_call("ID: 1, Name: User One, Timezone: UTC")
            mock_print.assert_any_call("ID: 2, Name: User Two, Timezone: Europe/London")

if __name__ == "__main__":
    unittest.main()
