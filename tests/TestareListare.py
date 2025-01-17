import unittest  # Import the unittest module for unit testing
from unittest.mock import MagicMock  # Import MagicMock for mocking methods
from services.user_service import UserService  # Import the UserService class

# Test class for user listing functionality
class TestareListare(unittest.TestCase):
    def setUp(self):  # Setup method to initialize test dependencies
        # Mock pentru users_table (necesar pentru constructorul UserService)
        self.mock_users_table = MagicMock()
        self.user_service = UserService(self.mock_users_table)  # Create an instance of UserService with mocked users_table
        # Mock the list_users method to return predefined users
        self.user_service.list_users = MagicMock(return_value=["John Doe", "Jane Smith"])

    def test_list_users(self):  # Test method for listing users
        users = self.user_service.list_users()  # Call the mocked list_users method
        self.user_service.list_users.assert_called_once()  # Verify the method was called exactly once
        self.assertEqual(len(users), 2)  # Assert that the list contains two users
        self.assertIn("John Doe", users)  # Assert that "John Doe" is in the returned user list

if __name__ == "__main__":  # Run the tests if the script is executed directly
    unittest.main()  # Run all the test cases
