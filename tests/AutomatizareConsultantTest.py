import unittest
from unittest.mock import patch
from data.storage import consultants, available_slots, appointments, users
from models.user import User
from services.appointment_service import AppointmentService
from services.user_service import UserService
from Database.database import users_table  # Import users_table to pass to UserService

class TestUnavailableConsultant(unittest.TestCase):
    def setUp(self):
        # Initialize the services with their dependencies
        self.user_service = UserService(users_table)  # Pass users_table to UserService
        self.appointment_service = AppointmentService(appointments, self.user_service)

        # Clear existing data to avoid conflicts during testing
        users.clear()
        consultants.clear()
        appointments.clear()
        available_slots.clear()

        # Add a user and an unavailable consultant
        users.append(User(1, "Alice", "UTC"))
        consultants.append("Bob (Finance)")
        available_slots["Bob (Finance)"] = []  # Consultant has no available slots

    @patch("builtins.input", side_effect=["Alice", "1", "1"])
    def test_create_appointment_with_unavailable_consultant(self, mock_input):
        """
        Test fails if the application allows creating an appointment with an unavailable consultant.
        """
        self.appointment_service.create_appointment()
        self.assertEqual(len(appointments), 0, "Appointment should not be created if the consultant is unavailable.")
