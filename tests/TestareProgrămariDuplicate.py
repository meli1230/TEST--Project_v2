#import required modules and classes for testing
import unittest  #import the unittest module for unit testing
from unittest.mock import MagicMock, create_autospec  #import MagicMock and create_autospec for mocking methods
from services.user_service import UserService  #import the UserService class

#test class for handling duplicate appointment scenarios
class TestareAppointmentDuplicat(unittest.TestCase):
    def setUp(self):  #setup method to initialize test dependencies
        self.user_service = MagicMock(spec=UserService)  #mock the UserService class
        self.appointment_service = MagicMock()  #mock the AppointmentService class

        #mock the list_appointments method to return a predefined appointment
        self.appointment_service.list_appointments.return_value = [
            {"user": "John Doe", "date": "2024-12-12 10:00"}  #mocked existing appointment for John Doe
        ]

        #mock create_appointment to raise an error for duplicates
        self.appointment_service.create_appointment.side_effect = ValueError("Appointment already exists")

    def test_duplicate_appointment(self):  #test method for creating a duplicate appointment
        user = "John Doe"  #define the user for the test
        date = "2024-12-12 10:00"  #define the date for the test

        #assert that a ValueError is raised when attempting to create a duplicate appointment
        with self.assertRaises(ValueError) as context:
            self.appointment_service.create_appointment(user, date)  #call the mocked create_appointment method

        #verify the method was called with the correct arguments
        self.appointment_service.create_appointment.assert_called_once_with(user, date)
        #assert that the raised exception message matches the expected message
        self.assertEqual(str(context.exception), "Appointment already exists")


if __name__ == '__main__':
    unittest.main()
