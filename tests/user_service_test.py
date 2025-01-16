#import required modules and classes for testing
import unittest  #import the unittest module for unit testing
from unittest.mock import patch  #import patch for mocking inputs
from data.storage import users  #import the global users list from storage
from models.user import User  #import the User model
from services.user_service import UserService  #import the UserService class

#test class for UserService functionality
class TestUserService(unittest.TestCase):
    def setUp(self):
        """Setup method to initialize test dependencies."""
        self.service = UserService()  #create an instance of UserService
        users.clear()  #clear the global users list to ensure a clean slate for testing

    @patch('builtins.input', side_effect=['Test User', '1'])  #mock user input for name and timezone
    def test_add_user_valid(self, mock_input):
        """Test adding a user with valid input."""
        self.service.add_user()  #call add_user method
        self.assertEqual(len(users), 1)  #assert that a user was added
        self.assertEqual(users[0].name, 'Test User')  #assert that the user's name matches
        self.assertEqual(users[0].timezone, 'UTC')  #assert that the default timezone is UTC

    @patch('builtins.input', side_effect=['123Invalid', '1'])  #mock invalid name
    def test_add_user_invalid_name(self, mock_input):
        """Test adding a user with invalid name."""
        self.service.add_user()  #call add_user method
        self.assertEqual(len(users), 0)  #assert that no user was added

    @patch('builtins.input', side_effect=['Test User', '99'])  #mock invalid timezone selection
    def test_add_user_invalid_timezone(self, mock_input):
        """Test adding a user with invalid timezone selection."""
        self.service.add_user()  #call add_user method
        self.assertEqual(len(users), 1)  #user is still added, but with default timezone
        self.assertEqual(users[0].timezone, 'UTC')  #assert timezone defaulted to UTC

    @patch('builtins.input', side_effect=['Test User'])  #mock user input for deletion
    def test_delete_user_valid(self, mock_input):
        """Test deleting a user with valid input."""
        user = User(1, 'Test User', 'UTC')  #create a user
        users.append(user)  #add the user to the list
        self.service.delete_user()  #call delete_user method
        self.assertEqual(len(users), 0)  #assert that the user was deleted

    @patch('builtins.input', side_effect=['Nonexistent User'])  #mock input for a nonexistent user
    def test_delete_user_not_found(self, mock_input):
        """Test deleting a nonexistent user."""
        with patch('builtins.print') as mock_print:  #mock print to capture output
            self.service.delete_user()  #call delete_user method
            mock_print.assert_any_call("User not found.")  #assert correct message was printed

    def test_list_users_empty(self):
        """Test listing users when no users are present."""
        with patch('builtins.print') as mock_print:  #mock print to capture output
            self.service.list_users()  #call list_users method
            mock_print.assert_any_call("No users found.")  #assert correct message was printed

    def test_list_users_with_data(self):
        """Test listing users when users are present."""
        user1 = User(1, 'User One', 'UTC')  #create user one
        user2 = User(2, 'User Two', 'Europe/London')  #create user two
        users.extend([user1, user2])  #add users to the list
        with patch('builtins.print') as mock_print:  #mock print to capture output
            self.service.list_users()  #call list_users method
            mock_print.assert_any_call("ID: 1, Name: User One, Timezone: UTC")  #assert user one details
            mock_print.assert_any_call("ID: 2, Name: User Two, Timezone: Europe/London")  #assert user two details

if __name__ == "__main__":  #run the tests if the script is executed directly
    unittest.main()  #execute all the tests