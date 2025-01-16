import unittest
from unittest.mock import patch
from data.storage import users
from models.user import User
from services.user_service import UserService


class TestUserServiceAutomation(unittest.TestCase):
    def setUp(self):
        """Curăță lista de utilizatori înainte de fiecare test."""
        self.user_service = UserService()
        users.clear()

    @patch("builtins.input", side_effect=["John Doe", "1"])  # Primul utilizator
    def test_add_duplicate_user(self, mock_input):
        """Test automatizat care eșuează pentru adăugarea unui utilizator duplicat."""
        # Adăugăm primul utilizator
        self.user_service.add_user()
        self.assertEqual(len(users), 1, "Ar trebui să fie un utilizator în listă.")

        # Încercăm să adăugăm același utilizator
        with patch("builtins.input", side_effect=["John Doe", "1"]):
            self.user_service.add_user()

        # Verificăm că utilizatorul duplicat nu a fost adăugat
        self.assertEqual(len(users), 1, "Utilizatorii cu nume duplicate nu ar trebui adăugați.")