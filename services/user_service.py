#from required modules and classes
from data.storage import users, TIMEZONES  #import the user data and timezone list
from models.user import User  #import the User model
from Database.database import list_users as db_list_users  # Importă funcția pentru listare din baza de date
from Database.database import delete_user as db_delete_user
from Database.database import add_user as db_add_user

#class to handle user-related functionality
import re  # Import regex module for name validation

class UserService:

    def __init__(self, users_table):
        self.users_table = users_table  # Conectează clasa la tabelul din baza de date

    # Method to add a new user
    def add_user(self, language):
        if language == "en":
            print("Enter user name:")
        elif language == "ro":
            print("Introduceți numele utilizatorului:")
        elif language == "fr":
            print("Entrez le nom de l'utilisateur:")

        name = input().strip()
        if not re.match("^[A-Za-z ]+$", name):
            if language == "en":
                print("Invalid name. Please use only letters and spaces.")
            elif language == "ro":
                print("Nume invalid. Vă rugăm să folosiți doar litere și spații.")
            elif language == "fr":
                print("Nom invalide. Veuillez utiliser uniquement des lettres et des espaces.")
            return

        existing_users = db_list_users()  # Fetch users from the database
        if any(user['name'].lower() == name.lower() for user in existing_users):  # Check for duplicates
            if language == "en":
                print(f"User with name '{name}' already exists! Please choose a different name.")
            elif language == "ro":
                print(f"Utilizatorul cu numele '{name}' există deja! Vă rugăm să alegeți un alt nume.")
            elif language == "fr":
                print(f"L'utilisateur avec le nom '{name}' existe déjà ! Veuillez choisir un autre nom.")
            return  # Exit if user already exists

        if language == "en":
            print("Available Time Zones:")
        elif language == "ro":
            print("Fusuri orare disponibile:")
        elif language == "fr":
            print("Fuseaux horaires disponibles:")

        for idx, tz in enumerate(TIMEZONES, 1):  # Enumerate timezones for better readability
            print(f"{idx}. {tz}")

        try:
            if language == "en":
                tz_choice = int(input("Choose your timezone: "))
            elif language == "ro":
                tz_choice = int(input("Alegeți fusul orar: "))
            elif language == "fr":
                tz_choice = int(input("Choisissez votre fuseau horaire: "))

            if tz_choice < 1 or tz_choice > len(TIMEZONES):
                raise ValueError()
            timezone = TIMEZONES[tz_choice - 1]
        except Exception:
            if language == "en":
                print("Invalid input. Defaulting to UTC.")
            elif language == "ro":
                print("Intrare invalidă. Se setează UTC implicit.")
            elif language == "fr":
                print("Entrée invalide. UTC sera utilisé par défaut.")
            timezone = "UTC"

        result = db_add_user(None, name, timezone)
        print(result)

    #method to list all users
    def list_users(self):
        users = db_list_users()  # Apelează funcția de listare din database.py
        if not users:  # Dacă lista este goală
            print("No users found.")  # Mesaj de eroare
        else:
            for user in users:  # Iterează prin utilizatori
                print(f"ID: {user['user_id']}, Name: {user['name']}, Timezone: {user['timezone']}")

    #method to list users for deletion
    def list_users(self, language):
        users = db_list_users()
        if not users:
            if language == "en":
                print("No users found.")
            elif language == "ro":
                print("Nu au fost găsiți utilizatori.")
            elif language == "fr":
                print("Aucun utilisateur trouvé.")
        else:
            for user in users:
                if language == "en":
                    print(f"ID: {user['user_id']}, Name: {user['name']}, Timezone: {user['timezone']}")
                elif language == "ro":
                    print(f"ID: {user['user_id']}, Nume: {user['name']}, Fus orar: {user['timezone']}")
                elif language == "fr":
                    print(f"ID: {user['user_id']}, Nom: {user['name']}, Fuseau horaire: {user['timezone']}")

    def delete_user(self, language, appointment_service):
        # List users to help the admin see available users
        self.list_users(language)
        if language == "en":
            username = input("Enter the name of the user to delete: ").strip()
        elif language == "ro":
            username = input("Introduceți numele utilizatorului de șters: ").strip()
        elif language == "fr":
            username = input("Entrez le nom de l'utilisateur à supprimer: ").strip()

        # Check if the user exists
        existing_users = db_list_users()
        user_to_delete = next((user for user in existing_users if user['name'].lower() == username.lower()), None)

        if user_to_delete:
            # Delete all appointments related to this user
            appointment_service.delete_appointments_for_user(user_to_delete['user_id'])

            # Delete the user
            result = db_delete_user(username)
            if result:
                if language == "en":
                    print(f"User {username} and their appointments were deleted successfully.")
                elif language == "ro":
                    print(f"Utilizatorul {username} și programările asociate au fost șterse cu succes.")
                elif language == "fr":
                    print(f"L'utilisateur {username} et ses rendez-vous ont été supprimés avec succès.")
            else:
                if language == "en":
                    print(f"An error occurred while deleting user {username}.")
                elif language == "ro":
                    print(f"A apărut o eroare la ștergerea utilizatorului {username}.")
                elif language == "fr":
                    print(f"Une erreur s'est produite lors de la suppression de l'utilisateur {username}.")
        else:
            if language == "en":
                print(f"User {username} does not exist.")
            elif language == "ro":
                print(f"Utilizatorul {username} nu există.")
            elif language == "fr":
                print(f"L'utilisateur {username} n'existe pas.")

