import unittest
from models.user import User
from data.storage import users

class TestMemoryOverload(unittest.TestCase):
    def test_memory_overload(self):
        """Test care gestioneaza suprasolicitarea."""
        for i in range(10**6):  # Adaugă un milion de utilizatori.
            users.append(User(i + 1, f"User{i + 1}", "UTC"))
        self.assertEqual(len(users), 10**6, "Ar trebui să fie un milion de utilizatori în listă.")