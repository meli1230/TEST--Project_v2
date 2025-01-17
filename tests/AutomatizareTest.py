import unittest
from unittest.mock import patch
from Database.database import users_table  # Import the users_table for database operations
from services.user_service import UserService


class TestUserServiceAutomation(unittest.TestCase):
    def setUp(self):
        """Clear the users table before each test."""
        self.user_service = UserService(users_table)  # Initialize with users_table
        users_table.truncate()  # Clear the database table for users

    @patch("builtins.input", side_effect=["John Doe", "1"])  # Valid name and valid timezone.
    def test_add_user_success(self, mock_input):
        """Automated test for adding a user."""
        self.user_service.add_user()
        users = users_table.all()
        self.assertEqual(len(users), 1, "There should be one user in the table.")
        self.assertEqual(users[0]["name"], "John Doe", "The user's name is incorrect.")
        self.assertEqual(users[0]["timezone"], "UTC", "The user's timezone is incorrect.")

    @patch("builtins.input", side_effect=["Nonexistent User"])  # Name that doesn't exist.
    def test_delete_nonexistent_user(self, mock_input):
        """Automated test for deleting a user that doesn't exist."""
        self.user_service.delete_user()
        users = users_table.all()
        self.assertEqual(len(users), 0, "The table should remain empty.")

    def test_list_users_empty(self):
        """Automated test for listing users when the table is empty."""
        with patch("builtins.print") as mock_print:
            self.user_service.list_users()
            mock_print.assert_called_with("No users found.")

    @patch("builtins.input", side_effect=["Jane Smith", "2"])  # Adding a new user.
    def test_add_and_delete_user(self, mock_input):
        """Automated test for adding and deleting a user."""
        self.user_service.add_user()
        users = users_table.all()
        self.assertEqual(len(users), 1, "The user should be added.")

        # Delete the user
        with patch("builtins.input", side_effect=["Jane Smith"]):
            self.user_service.delete_user()
        users = users_table.all()
        self.assertEqual(len(users), 0, "The table should be empty after deleting the user.")


if __name__ == "__main__":
    unittest.main()
