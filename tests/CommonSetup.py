import unittest
from unittest.mock import MagicMock
from Database.database import users_table
from services.user_service import UserService

class CommonSetup(unittest.TestCase):
    def setUp(self):
        """
        Sets up a common UserService with the required users_table.
        """
        self.user_service = UserService(users_table)  # Pass the required users_table
        users_table.truncate()  # Ensure the table is cleared before each test
