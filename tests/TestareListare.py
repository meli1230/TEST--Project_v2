import unittest  #import the unittest module for unit testing
from unittest.mock import MagicMock  #import MagicMock for mocking methods
from services.user_service import UserService  #import the UserService class

#test class for user listing functionality
class TestareListare(unittest.TestCase):
    def setUp(self):  #setup method to initialize test dependencies
        self.user_service = UserService()  #create an instance of UserService
        self.user_service.list_users = MagicMock(return_value=["John Doe", "Jane Smith"])  #mock the list_users method to return predefined users

    def test_list_users(self):  #test method for listing users
        users = self.user_service.list_users()  #call the mocked list_users method
        self.user_service.list_users.assert_called_once()  #verify the method was called exactly once
        self.assertEqual(len(users), 2)  #assert that the list contains two users
        self.assertIn("John Doe", users)  #assert that "John Doe" is in the returned user list

if __name__ == "__main__":  #run the tests if the script is executed directly
    unittest.main()  #run all the test cases