import unittest
from unittest.mock import patch
from Database.database import users_table  # Import users_table for database assertions
from services.user_service import UserService


class TestUserServiceAutomation(unittest.TestCase):
    def setUp(self):
        """Clear the users table in the database before each test."""
        self.user_service = UserService(users_table)  # Initialize with users_table
        users_table.truncate()  # Clear the database table for users

    @patch("builtins.input", side_effect=["John Doe", "1"])  # Input for the first user
    def test_add_duplicate_user(self, mock_input):
        """Automated test that fails when trying to add a duplicate user."""
        # Add the first user
        self.user_service.add_user()
        self.assertEqual(len(users_table.all()), 1, "There should be one user in the database.")

        # Attempt to add the same user again
        with patch("builtins.input", side_effect=["John Doe", "1"]):
            self.user_service.add_user()

        # Verify that the duplicate user was not added
        self.assertEqual(len(users_table.all()), 1, "Duplicate users should not be added.")
