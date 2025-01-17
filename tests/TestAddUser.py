import unittest
from unittest.mock import patch
from Database.database import users_table  # Import the users_table for database operations
from data.storage import users, TIMEZONES
from services.user_service import UserService


class TestAddUser(unittest.TestCase):
    def setUp(self):
        """
        Initialize the UserService and clear the users table to ensure a clean slate for testing.
        """
        self.user_service = UserService(users_table)  # Initialize UserService with the required users_table
        users_table.truncate()  # Clear the users table in the database
        users.clear()  # Clear the in-memory users list

    @patch("builtins.input", side_effect=["", "1"])  # Empty name but valid timezone selection.
    def test_add_user_fails_with_empty_name(self, mock_input):
        """
        Test that adding a user with an empty name does not add the user to the database.
        """
        self.user_service.add_user()  # Attempt to add a user with an empty name.
        self.assertEqual(len(users_table.all()), 0, "A user should not be added with an empty name.")

    @patch("builtins.input", side_effect=["Test User", "99"])  # Valid name but invalid timezone selection.
    def test_add_user_defaults_to_utc_with_invalid_timezone(self, mock_input):
        """
        Test that adding a user with a valid name but an invalid timezone defaults to UTC.
        """
        self.user_service.add_user()  # Attempt to add a user with an invalid timezone selection.
        users = users_table.all()  # Retrieve users from the database.
        self.assertEqual(len(users), 1, "A user should be added if the name is valid.")
        self.assertEqual(users[0]["timezone"], "UTC", "The timezone should default to UTC if the input is invalid.")


if __name__ == "__main__":
    unittest.main()
