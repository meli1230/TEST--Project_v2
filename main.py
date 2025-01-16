from Database.database import users_table, appointments_table  # Importă tabelele din database.py
from services.user_service import UserService  #import the UserService class
from services.appointment_service import AppointmentService  #import the AppointmentService class

def select_language():
    print("Select your language / Alegeți limba / Choisissez la langue:")
    print("1. English")
    print("2. Română")
    print("3. Français")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            return "en"
        elif choice == "2":
            return "ro"
        elif choice == "3":
            return "fr"
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def main_menu(language):
    if language == "en":
        print("\n--- Appointment Scheduling App ---")
        print("1. Add User")
        print("2. Delete User")
        print("3. List Users")
        print("4. Make an Appointment")
        print("5. View Appointments")
        print("6. Exit")
        return input("Choose an option: ")
    elif language == "ro":
        print("\n--- Aplicație de Programare ---")
        print("1. Adaugă Utilizator")
        print("2. Șterge Utilizator")
        print("3. Listează Utilizatori")
        print("4. Creează o Programare")
        print("5. Vezi Programări")
        print("6. Ieșire")
        return input("Alegeți o opțiune: ")
    elif language == "fr":
        print("\n--- Application de Planification ---")
        print("1. Ajouter un Utilisateur")
        print("2. Supprimer un Utilisateur")
        print("3. Lister les Utilisateurs")
        print("4. Planifier un Rendez-vous")
        print("5. Voir les Rendez-vous")
        print("6. Quitter")
        return input("Choisissez une option: ")

def main():  # Main function to run the application
    language = select_language()  # Ask the user to select a language
    user_service = UserService(users_table)  # Create an instance of UserService
    appointment_service = AppointmentService(appointments_table, user_service)  # Create an instance of AppointmentService with user_service

    while True:  # Start an infinite loop for the main menu
        choice = main_menu(language)  # Pass the selected language to display the main menu
        if choice == "1":  # If the choice is 1
            user_service.add_user(language)  # Call the add_user method with the language
        elif choice == "2":  # If the choice is 2
            user_service.delete_user(language)  # Call the delete_user method with the language
        elif choice == "3":  # If the choice is 3
            user_service.list_users(language)  # Call the list_users method with the language
        elif choice == "4":  # If the choice is 4
            appointment_service.create_appointment(language)  # Call the create_appointment method with the language
        elif choice == "5":  # If the choice is 5
            appointment_service.list_appointments(language)  # Call the list_appointments method with the language
        elif choice == "6":  # If the choice is 6
            if language == "en":
                print("Goodbye!")  # Print a goodbye message
            elif language == "ro":
                print("La revedere!")  # Print a goodbye message in Romanian
            elif language == "fr":
                print("Au revoir!")  # Print a goodbye message in French
            break  # Exit the loop and end the program
        else:  # If the choice is invalid
            if language == "en":
                print("Invalid choice. Please try again.")  # Print an error message in English
            elif language == "ro":
                print("Opțiune invalidă. Vă rugăm să încercați din nou.")  # Print an error message in Romanian
            elif language == "fr":
                print("Choix invalide. Veuillez réessayer.")  # Print an error message in French


if __name__ == "__main__":  #run the program only if the script is executed directly
    main()  #call the main function