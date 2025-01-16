#from required modules and classes
from data.storage import users, TIMEZONES  #import the user data and timezone list
from models.user import User  #import the User model
from Database.database import list_users as db_list_users  # Importă funcția pentru listare din baza de date
from Database.database import delete_user as db_delete_user
from Database.database import add_user as db_add_user

import re

#class to handle user-related functionality
import re  # Import regex module for name validation

class UserService:

    def __init__(self, users_table):
        self.users_table = users_table  # Conectează clasa la tabelul din baza de date

    # Method to add a new user
    def add_user(self):
        # Prompt the user to input their name
        name = input("Enter user name: ").strip()

        # Validate the name: only allow alphabetic characters and spaces
        if not re.match("^[A-Za-z ]+$", name):
            print("Invalid name. Names should not contain numbers or special characters.")
            return  # Exit the method if the name is invalid

        # Display available time zones for selection
        print("Available Time Zones:")
        for idx, tz in enumerate(TIMEZONES, 1):  # Enumerate timezones for better readability
            print(f"{idx}. {tz}")

        # Prompt the user to select their timezone
        try:
            tz_choice = int(input("Choose your timezone (enter the number): "))
            if tz_choice < 1 or tz_choice > len(TIMEZONES):  # Validate the timezone choice
                raise ValueError("Invalid choice.")
            timezone = TIMEZONES[tz_choice - 1]  # Map the choice to the corresponding timezone
        except Exception as e:  # Handle invalid inputs gracefully
            print(f"Invalid input: {e}. Defaulting to UTC.")  # Inform the user and default to UTC
            timezone = "UTC"  # Assign default timezone if input is invalid

        # Generate a unique user ID and create the new user
        user_id = len(users) + 1
        user = User(user_id, name, timezone)  # Create a new User instance

        result = db_add_user(None, name, timezone)  # Transmite `None` pentru `user_id`, deoarece este generat automat.
        print(result)

        #users.append(user)  # Add the new user to the users list

        # Confirm successful user addition
        #print(f"User {name} added successfully with timezone {timezone}.")

    #method to delete a user
    def delete_user(self):
        self.list_users_when_delete()  #list all users for selection during deletion
        username = input("Enter user name to delete: ")  #prompt the user to input the name of the user to delete
        # Call the database function to delete the user
        result = db_delete_user(username)
        print(result)  # Print the result of the delete operation

    #method to list all users
    def list_users(self):
        users = db_list_users()  # Apelează funcția de listare din database.py
        if not users:  # Dacă lista este goală
            print("No users found.")  # Mesaj de eroare
        else:
            for user in users:  # Iterează prin utilizatori
                print(f"ID: {user['user_id']}, Name: {user['name']}, Timezone: {user['timezone']}")

    #method to list users for deletion
    def list_users_when_delete(self):
        users = db_list_users()  # Folosește funcția care accesează utilizatorii din baza de date
        if not users:  # Verifică dacă lista este goală
            print("No users found.")  # Afișează un mesaj dacă nu există utilizatori
            return
        for user in users:  # Iterează prin utilizatorii din baza de date
            print(f"ID: {user['user_id']}, Name: {user['name']}, Timezone: {user['timezone']}")