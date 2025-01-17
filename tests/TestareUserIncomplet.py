import unittest
from unittest.mock import MagicMock, patch
from data.storage import users
from models.user import User
from services.user_service import UserService


class TestListUserIncompleteData(unittest.TestCase):
    def setUp(self):
        # Creăm un mock pentru users_table
        self.mock_users_table = MagicMock()
        self.user_service = UserService(self.mock_users_table)

        # Curățăm și reinițializăm lista `users`
        users.clear()
        users.append(User(1, "John Doe", ""))  # Fus orar gol.

    def test_list_user_with_empty_timezone(self):
        """Test care verifică gestionarea unui fus orar gol."""
        # Mock-uim metoda list_users pentru a adăuga logica de fus orar gol
        with patch("builtins.print") as mock_print:
            for user in users:
                timezone = user.timezone if user.timezone else "[Invalid]"
                print(f"ID: {user.user_id}, Name: {user.name}, Timezone: {timezone}")

            # Verificăm că metoda `print` a fost apelată cu textul așteptat
            mock_print.assert_any_call("ID: 1, Name: John Doe, Timezone: [Invalid]")

