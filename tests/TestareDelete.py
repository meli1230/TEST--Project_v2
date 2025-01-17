# tests/user_service_test.py
import unittest
from unittest.mock import patch, MagicMock
from Database.database import users_table  # Import the users_table for database operations
from services.user_service import UserService


class TestUserService(unittest.TestCase):
    def setUp(self):
        """Prepare the test environment."""
        self.mock_users_table = MagicMock()  # Create a mock for the users_table
        self.service = UserService(self.mock_users_table)  # Pass the mock to UserService
        users_table.truncate()  # Clear the database for each test

    @patch('builtins.input', side_effect=['Test User', '1'])
    def test_add_user_valid(self, mock_input):
        """Test adding a valid user."""
        self.service.add_user()  # Add the user
        self.mock_users_table.insert.assert_called_once()  # Check if the insert method was called
        args, kwargs = self.mock_users_table.insert.call_args
        self.assertEqual(kwargs["name"], "Test User")
        self.assertEqual(kwargs["timezone"], "UTC")

    def test_delete_user_valid(self):
        """Test deleting a user."""
        self.mock_users_table.delete.return_value = True  # Mock delete_user response
        self.service.delete_user('Test User')  # Delete the user
        self.mock_users_table.delete.assert_called_once_with('Test User')  # Check if delete was called

    def test_list_users_empty(self):
        """Test listing when no users exist."""
        self.mock_users_table.all.return_value = []  # Mock an empty users table
        with patch('builtins.print') as mock_print:
            self.service.list_users()
            mock_print.assert_any_call("No users found.")

    def test_list_users_with_data(self):
        """Test listing existing users."""
        self.mock_users_table.all.return_value = [
            {"user_id": 1, "name": "User One", "timezone": "UTC"},
            {"user_id": 2, "name": "User Two", "timezone": "Europe/London"}
        ]  # Mock users table data
        with patch('builtins.print') as mock_print:
            self.service.list_users()
            mock_print.assert_any_call("ID: 1, Name: User One, Timezone: UTC")
            mock_print.assert_any_call("ID: 2, Name: User Two, Timezone: Europe/London")


if __name__ == "__main__":
    unittest.main()
