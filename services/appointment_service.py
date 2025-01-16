from Database.database import appointments_table
from data.storage import consultants, available_slots  # Eliminat lista `users`
from models.appointment import Appointment  # Import the Appointment model
from utils.timezone import convert_to_timezone  # Import a utility function for timezone conversion
from Database.database import list_users as db_list_users  # Import list_users direct din baza de date
from Database.database import add_appointment
from Database.database import list_appointments as db_list_appointments
import re  # Import regular expressions module for input validation

# Service class to handle appointment-related functionality
class AppointmentService:
    # Constructor for the AppointmentService class
    def __init__(self, appointments_table, user_service):
        self.appointments_table = appointments_table  # Store the appointments table
        self.user_service = user_service  # Initialize with a user service for user-related operations

    # Method to create a new appointment
    def create_appointment(self):
        try:
            users = db_list_users()  # Fetch users directly from the database
            if not users:
                print("No users found.")
                return

            # List all users
            for user in users:
                print(f"ID: {user['user_id']}, Name: {user['name']}, Timezone: {user['timezone']}")

            # Ask for user name
            while True:
                user_name = input("Enter user name: ").strip()
                # Validate input using regex (letters and spaces only)
                if not re.match(r'^[a-zA-Z\u00C0-\u017F\s]+$', user_name):
                    print("Invalid name. Please use only letters and spaces.")
                    continue

                user = next((u for u in users if u['name'].lower() == user_name.lower()), None)
                if not user:
                    print("User not found. Please try again.")
                    continue
                break

            print("Available Consultants:")
            for idx, consultant in enumerate(consultants, 1):
                print(f"{idx}. {consultant}")

            while True:
                try:
                    consultant_idx = int(input("Choose consultant: ")) - 1
                    if consultant_idx not in range(len(consultants)):
                        raise ValueError("Invalid consultant index.")
                    consultant = consultants[consultant_idx]
                    break
                except ValueError as e:
                    print(e)

            print("Available slots:")
            slots = available_slots.get(consultant, [])
            if not slots:
                print(f"No slots available for {consultant}.")
                return

            while True:
                try:
                    for idx, slot in enumerate(slots, 1):
                        print(f"{idx}. {slot}")

                    slot_idx = int(input("Choose a slot: ")) - 1
                    if slot_idx not in range(len(slots)):
                        raise ValueError("Invalid slot index.")
                    chosen_slot = slots.pop(slot_idx)
                    break
                except ValueError as e:
                    print(e)

            customer_time = convert_to_timezone(chosen_slot, "UTC", user['timezone'])
            mentor_time = convert_to_timezone(chosen_slot, "UTC", "Europe/Bucharest")

            appointment = Appointment(user, consultant, customer_time, mentor_time)

            add_appointment({
                'user_id': user['user_id'],
                'name': user['name'],
                'timezone': user['timezone']
            }, consultant, customer_time, mentor_time)

            print("Appointment created successfully.")
            print(f"Appointment time in your timezone: {customer_time}")
            print(f"Appointment time in Bucharest timezone: {mentor_time}")

        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting gracefully.")

    # Method to list all scheduled appointments
    def list_appointments(self):
        try:
            appointments = db_list_appointments()  # Fetch appointments from the database
            if not appointments:
                print("No appointments scheduled.")
                return

            for appt in appointments:
                print(f"User: {appt['user']['name']}, Consultant: {appt['consultant']}")
                print(f"  Time in Customer's Timezone: {appt['customer_time']}")
                print(f"  Time in Mentor's Timezone: {appt['mentor_time']}")
                print("-" * 40)

        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting gracefully.")