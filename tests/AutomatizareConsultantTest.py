import unittest
from unittest.mock import patch
from data.storage import consultants, available_slots, appointments, users
from models.user import User
from services.appointment_service import AppointmentService
from services.user_service import UserService

class TestUnavailableConsultant(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()
        self.appointment_service = AppointmentService(self.user_service)
        users.clear()
        consultants.clear()
        appointments.clear()
        available_slots.clear()

        # Adaugă un utilizator și un consultant indisponibil
        users.append(User(1, "Alice", "UTC"))
        consultants.append("Bob (Finance)")
        available_slots["Bob (Finance)"] = []  # Consultantul nu are sloturi disponibile

    @patch("builtins.input", side_effect=["Alice", "1", "1"])
    def test_create_appointment_with_unavailable_consultant(self, mock_input):
        """Test care eșuează dacă aplicația permite crearea unei programări cu un consultant indisponibil."""
        self.appointment_service.create_appointment()
        self.assertEqual(len(appointments), 0, "Programarea nu ar trebui creată dacă consultantul este indisponibil.")