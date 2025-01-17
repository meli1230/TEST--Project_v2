import unittest
from unittest.mock import patch
from io import StringIO
from Database.database import users_table  # Import users_table for database operations
from services.user_service import UserService


class TestListUsersFormat(unittest.TestCase):
    """
    Tests the `list_users` method from the `UserService` class to ensure it
    displays user details in a specific format.
    """

    def setUp(self):
        """
        Initial setup for the test:
        - Creates an instance of the `UserService` class.
        - Clears the users table (`users_table`) to start with a clean slate.
        """
        self.user_service = UserService(users_table)
        users_table.truncate()  # Clear the users table in the database

    def test_list_users_format(self):
        """
        Tests if the `list_users` method displays user details in the correct format.
        - Creates a mock user.
        - Adds the user to the database.
        - Captures the output of the `list_users` method.
        - Verifies the output contains the correct user details.
        """
        # Add a user directly to the database
        users_table.insert({"user_id": 1, "name": "John Doe", "timezone": "UTC"})

        # Capture the output of `list_users`
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.user_service.list_users()
            output = mock_stdout.getvalue().strip()

        # Verify if the correct message format is present in the output
        self.assertIn("ID: 1, Name: John Doe, Timezone: UTC", output)


if __name__ == "__main__":
    unittest.main()
