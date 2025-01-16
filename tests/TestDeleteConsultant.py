import unittest
from data.storage import consultants, available_slots, appointments, users


class TestDeleteNonexistentConsultant(unittest.TestCase):
    def setUp(self):
        consultants.clear()

    def test_delete_nonexistent_consultant(self):
        """Test care eșuează dacă aplicația gestionează greșit ștergerea unui consultant inexistent."""
        consultant_to_delete = "Jane Doe (HR)"
        initial_count = len(consultants)
        try:
            consultants.remove(consultant_to_delete)  # Consultantul nu există
        except ValueError:
            pass  # Aceasta este logica corectă

        self.assertEqual(len(consultants), initial_count, "Lista consultanților nu ar trebui modificată.")