import unittest
from unittest.mock import patch
from data.storage import users
from models.user import User
from services.user_service import UserService


class TestUserServiceUnicode(unittest.TestCase):
    def setUp(self):
        self.service = UserService()  #create an instance of UserService
        users.clear()  #clear the global users list to ensure a clean slate for testing

    @patch('builtins.input', side_effect=['张伟', '1'])  #mock user input with a Unicode name and valid timezone selection
    def test_add_user_with_unicode_name(self, mock_input):
        """Test adding a user with a Unicode name."""
        self.service.add_user()  #call add_user method
        self.assertEqual(len(users), 1)  #assert that a user was added
        self.assertEqual(users[0].name, '张伟')  #assert that the user's name matches the Unicode input
        self.assertEqual(users[0].timezone, 'UTC')  #assert that the timezone is set correctly

    @patch('builtins.input', side_effect=['Éléonore', '1'])  #mock input with another Unicode name
    def test_add_user_with_unicode_name_accented(self, mock_input):
        """Test adding a user with an accented Unicode name."""
        self.service.add_user()  #call add_user method
        self.assertEqual(len(users), 1)  #assert that a user was added
        self.assertEqual(users[0].name, 'Éléonore')  #assert that the user's name matches
        self.assertEqual(users[0].timezone, 'UTC')  #assert the timezone

if __name__ == "__main__":  #run the tests if the script is executed directly
    unittest.main()