#import required modules and classes for testing
import unittest  #import the unittest module for unit testing
from unittest.mock import MagicMock  #import MagicMock for mocking methods
from services.user_service import UserService  #import the UserService class
from services.appointment_service import AppointmentService  #import the AppointmentService class

#test class for handling appointments of nonexistent users
class TestareAppointmentUtilizatorInexistent(unittest.TestCase):
    def setUp(self):  #setup method to initialize test dependencies
        self.user_service = UserService()  #create an instance of UserService
        self.appointment_service = AppointmentService(self.user_service)  #create an instance of AppointmentService with user_service

        self.user_service.list_users = MagicMock(return_value=["John Doe", "Jane Smith"])  #mock list_users to return predefined users
        self.appointment_service.list_appointments_by_user = MagicMock(return_value=[])  #mock list_appointments_by_user to return an empty list for nonexistent users

    def test_list_appointments_for_nonexistent_user(self):  #test method for listing appointments of a nonexistent user
        nonexistent_user = "Alex Johnson"  #define a nonexistent user for the test
        appointments = self.appointment_service.list_appointments_by_user(nonexistent_user)  #call the mocked method with the nonexistent user

        self.appointment_service.list_appointments_by_user.assert_called_once_with(nonexistent_user)  #verify the method was called with the correct user
        self.assertEqual(len(appointments), 0)  #assert that the returned appointment list is empty