import unittest
import threading
from unittest.mock import patch
from data.storage import users
from models.user import User
from services.user_service import UserService

class TestConcurrentDeletion(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()
        users.clear()
        # Adaugă 100 de utilizatori
        for i in range(100):
            users.append(User(i + 1, f"User{i + 1}", "UTC"))

    def test_concurrent_user_deletion(self):
        """Test pentru ștergerea simultană a utilizatorilor."""

        def delete_user():
            if users:
                users.pop(0)

        threads = []
        for _ in range(100):  # Creează 100 de fire pentru ștergere.
            thread = threading.Thread(target=delete_user)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        self.assertEqual(len(users), 0, "Lista ar trebui să fie goală după ștergere.")