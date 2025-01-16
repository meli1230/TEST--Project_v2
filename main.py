from Database.database import users_table, appointments_table  # Importă tabelele din database.py
from services.user_service import UserService  #import the UserService class
from services.appointment_service import AppointmentService  #import the AppointmentService class

def main_menu():  #function to display the main menu and get user input
    print("\n--- Appointment Scheduling App ---")  #display the application title
    print("1. Add User")  #option to add a user
    print("2. Delete User")  #option to delete a user
    print("3. List Users")  #option to list all users
    print("4. Make an Appointment")  #option to create an appointment
    print("5. View Appointments")  #option to view all appointments
    print("6. Exit")  #option to exit the application
    return input("Choose an option: ")  #return the user's choice as input

def main():  #main function to run the application
    user_service = UserService(users_table)  #create an instance of UserService
    appointment_service = AppointmentService(appointments_table, user_service) #create an instance of AppointmentService with user_service

    while True:  #start an infinite loop for the main menu
        choice = main_menu()  #display the main menu and get the user's choice
        if choice == "1":  #if the choice is 1
            user_service.add_user()  #call the add_user method
        elif choice == "2":  #if the choice is 2
            user_service.delete_user()  #call the delete_user method
        elif choice == "3":  #if the choice is 3
            user_service.list_users()  #call the list_users method
        elif choice == "4":  #if the choice is 4
            appointment_service.create_appointment()  #call the create_appointment method
        elif choice == "5":  #if the choice is 5
            appointment_service.list_appointments()  #call the list_appointments method
        elif choice == "6":  #if the choice is 6
            print("Goodbye!")  #print a goodbye message
            break  #exit the loop and end the program
        else:  #if the choice is invalid
            print("Invalid choice. Please try again.")  #print an error message

if __name__ == "__main__":  #run the program only if the script is executed directly
    main()  #call the main function