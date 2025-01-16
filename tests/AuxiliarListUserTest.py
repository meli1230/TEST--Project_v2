import unittest
from data.storage import users
from models.user import User
from services.user_service import UserService

class TestListUsersFormat(unittest.TestCase):
    """
    Testează metoda `list_users` din clasa `UserService` pentru a verifica dacă
    afișează corect detaliile utilizatorilor într-un format specific.
    """

    def setUp(self):
        """
        Configurare inițială pentru test:
        - Creează o instanță a clasei `UserService`.
        - Curăță lista de utilizatori (`users`) pentru a începe cu un mediu curat.
        """
        self.user_service = UserService()
        users.clear()

    def test_list_users_format(self):
        """
        Testează dacă metoda `list_users` afișează detaliile utilizatorilor în formatul corect.
        - Creează un utilizator fictiv.
        - Adaugă utilizatorul în lista globală `users`.
        - Capturează log-urile generate de metoda `list_users`.
        - Verifică dacă mesajul logat conține informațiile corecte despre utilizator.
        """
        # Creează un utilizator și îl adaugă în lista globală `users`
        user = User(1, "John Doe", "UTC")
        users.append(user)

        # Capturează log-urile generate de metoda `list_users`
        with self.assertLogs() as log:
            self.user_service.list_users()

        # Verifică dacă formatul corect al mesajului este prezent în log-uri
        self.assertIn("ID: 1, Name: John Doe, Timezone: UTC", log.output[0])