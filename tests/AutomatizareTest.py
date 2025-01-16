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

    @patch("builtins.input", side_effect=["John Doe", "1"])  # Nume valid și fus orar valid.
    def test_add_user_success(self, mock_input):
        """Test automatizat pentru adăugarea unui utilizator."""
        self.user_service.add_user()
        self.assertEqual(len(users), 1, "Ar trebui să fie un utilizator în listă.")
        self.assertEqual(users[0].name, "John Doe", "Numele utilizatorului nu este corect.")
        self.assertEqual(users[0].timezone, "UTC", "Fusul orar al utilizatorului nu este corect.")

    @patch("builtins.input", side_effect=["Nonexistent User"])  # Nume care nu există.
    def test_delete_nonexistent_user(self, mock_input):
        """Test automatizat pentru ștergerea unui utilizator care nu există."""
        self.user_service.delete_user()
        self.assertEqual(len(users), 0, "Lista ar trebui să rămână goală.")

    def test_list_users_empty(self):
        """Test automatizat pentru listarea utilizatorilor când lista este goală."""
        with patch("builtins.print") as mock_print:
            self.user_service.list_users()
            mock_print.assert_called_with("No users found.")

    @patch("builtins.input", side_effect=["Jane Smith", "2"])  # Adăugare utilizator nou.
    def test_add_and_delete_user(self, mock_input):
        """Test automatizat pentru adăugarea și ștergerea unui utilizator."""
        self.user_service.add_user()
        self.assertEqual(len(users), 1, "Utilizatorul ar trebui să fie adăugat.")

        # Ștergere utilizator
        with patch("builtins.input", side_effect=["Jane Smith"]):
            self.user_service.delete_user()
        self.assertEqual(len(users), 0, "Lista ar trebui să fie goală după ștergerea utilizatorului.")


if __name__ == "__main__":
    unittest.main()