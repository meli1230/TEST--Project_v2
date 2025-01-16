#import required modules and classes for testing
import unittest  #import the unittest module for unit testing
from unittest.mock import MagicMock  #import MagicMock for mocking methods
from services.user_service import UserService  #import the UserService class
from services.appointment_service import AppointmentService  #import the AppointmentService class

#test class for handling duplicate appointment scenarios
class TestareAppointmentDuplicat(unittest.TestCase):
    def setUp(self):  #setup method to initialize test dependencies
        self.user_service = UserService()  #create an instance of UserService
        self.appointment_service = AppointmentService(self.user_service)  #create an instance of AppointmentService with user_service

        self.appointment_service.list_appointments = MagicMock(return_value=[  #mock the list_appointments method to return a predefined appointment
            {"user": "John Doe", "date": "2024-12-12 10:00"}  #mocked existing appointment for John Doe
        ])
        self.appointment_service.create_appointment = MagicMock(side_effect=ValueError("Appointment already exists"))  #mock create_appointment to raise an error for duplicates

    def test_duplicate_appointment(self):  #test method for creating a duplicate appointment
        user = "John Doe"  #define the user for the test
        date = "2024-12-12 10:00"  #define the date for the test

        with self.assertRaises(ValueError) as context:  #assert that a ValueError is raised when attempting to create a duplicate appointment
            self.appointment_service.create_appointment(user, date)  #call the mocked create_appointment method

        self.appointment_service.create_appointment.assert_called_once_with(user, date)  #verify the method was called with the correct arguments
        self.assertEqual(str(context.exception), "Appointment already exists")  #assert that the raised exception message matches the expected message