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
    def create_appointment(self, language):
        try:
            users = db_list_users()
            if not users:
                if language == "en":
                    print("No users found.")
                elif language == "ro":
                    print("Nu au fost găsiți utilizatori.")
                elif language == "fr":
                    print("Aucun utilisateur trouvé.")
                return

            # List all users
            for user in users:
                if language == "en":
                    print(f"ID: {user['user_id']}, Name: {user['name']}, Timezone: {user['timezone']}")
                elif language == "ro":
                    print(f"ID: {user['user_id']}, Nume: {user['name']}, Fus orar: {user['timezone']}")
                elif language == "fr":
                    print(f"ID: {user['user_id']}, Nom: {user['name']}, Fuseau horaire: {user['timezone']}")

            # Ask for user name
            while True:
                if language == "en":
                    user_name = input("Enter user name: ").strip()
                elif language == "ro":
                    user_name = input("Introduceți numele utilizatorului: ").strip()
                elif language == "fr":
                    user_name = input("Entrez le nom de l'utilisateur: ").strip()

                if not re.match(r'^[a-zA-Z\u00C0-\u017F\s]+$', user_name):
                    if language == "en":
                        print("Invalid name. Please use only letters and spaces.")
                    elif language == "ro":
                        print("Nume invalid. Vă rugăm să folosiți doar litere și spații.")
                    elif language == "fr":
                        print("Nom invalide. Veuillez utiliser uniquement des lettres et des espaces.")
                    continue

                user = next((u for u in users if u['name'].lower() == user_name.lower()), None)
                if not user:
                    if language == "en":
                        print("User not found. Please try again.")
                    elif language == "ro":
                        print("Utilizatorul nu a fost găsit. Vă rugăm să încercați din nou.")
                    elif language == "fr":
                        print("Utilisateur introuvable. Veuillez réessayer.")
                    continue
                break

            if language == "en":
                print("Available Consultants:")
            elif language == "ro":
                print("Consultanți disponibili:")
            elif language == "fr":
                print("Consultants disponibles:")

            for idx, consultant in enumerate(consultants, 1):
                print(f"{idx}. {consultant}")

            while True:
                try:
                    if language == "en":
                        consultant_idx = int(input("Choose consultant: ")) - 1
                    elif language == "ro":
                        consultant_idx = int(input("Alegeți consultantul: ")) - 1
                    elif language == "fr":
                        consultant_idx = int(input("Choisissez un consultant: ")) - 1

                    if consultant_idx not in range(len(consultants)):
                        raise ValueError()
                    consultant = consultants[consultant_idx]
                    break
                except ValueError:
                    if language == "en":
                        print("Invalid consultant index.")
                    elif language == "ro":
                        print("Index consultant invalid.")
                    elif language == "fr":
                        print("Index du consultant invalide.")

            if language == "en":
                print("Available slots:")
            elif language == "ro":
                print("Sloturi disponibile:")
            elif language == "fr":
                print("Créneaux disponibles:")

            slots = available_slots.get(consultant, [])
            if not slots:
                if language == "en":
                    print(f"No slots available for {consultant}.")
                elif language == "ro":
                    print(f"Nu sunt sloturi disponibile pentru {consultant}.")
                elif language == "fr":
                    print(f"Aucun créneau disponible pour {consultant}.")
                return

            while True:
                try:
                    for idx, slot in enumerate(slots, 1):
                        print(f"{idx}. {slot}")

                    if language == "en":
                        slot_idx = int(input("Choose a slot: ")) - 1
                    elif language == "ro":
                        slot_idx = int(input("Alegeți un slot: ")) - 1
                    elif language == "fr":
                        slot_idx = int(input("Choisissez un créneau: ")) - 1

                    if slot_idx not in range(len(slots)):
                        raise ValueError()
                    chosen_slot = slots.pop(slot_idx)
                    break
                except ValueError:
                    if language == "en":
                        print("Invalid slot index.")
                    elif language == "ro":
                        print("Index slot invalid.")
                    elif language == "fr":
                        print("Index du créneau invalide.")

            customer_time = convert_to_timezone(chosen_slot, "UTC", user['timezone'])
            mentor_time = convert_to_timezone(chosen_slot, "UTC", "Europe/Bucharest")

            appointment = Appointment(user, consultant, customer_time, mentor_time)

            add_appointment({
                'user_id': user['user_id'],
                'name': user['name'],
                'timezone': user['timezone']
            }, consultant, customer_time, mentor_time)

            if language == "en":
                print("Appointment created successfully.")
                print(f"Appointment time in your timezone: {customer_time}")
                print(f"Appointment time in Bucharest timezone: {mentor_time}")
            elif language == "ro":
                print("Programarea a fost creată cu succes.")
                print(f"Oră programare în fusul dvs. orar: {customer_time}")
                print(f"Oră programare în fusul orar București: {mentor_time}")
            elif language == "fr":
                print("Rendez-vous créé avec succès.")
                print(f"Heure du rendez-vous dans votre fuseau horaire: {customer_time}")
                print(f"Heure du rendez-vous dans le fuseau horaire de Bucarest: {mentor_time}")

        except KeyboardInterrupt:
            if language == "en":
                print("\nProgram interrupted by user. Exiting gracefully.")
            elif language == "ro":
                print("\nProgramul a fost întrerupt de utilizator. Ieșire în siguranță.")
            elif language == "fr":
                print("\nProgramme interrompu par l'utilisateur. Fermeture en douceur.")

    # Method to list all scheduled appointments
    def list_appointments(self, language):
        try:
            appointments = db_list_appointments()  # Fetch appointments from the database
            if not appointments:
                if language == "en":
                    print("No appointments scheduled.")
                elif language == "ro":
                    print("Nu sunt programări programate.")
                elif language == "fr":
                    print("Aucun rendez-vous planifié.")
                return

            for appt in appointments:
                if language == "en":
                    print(f"User: {appt['user']['name']}, Consultant: {appt['consultant']}")
                    print(f"  Time in Customer's Timezone: {appt['customer_time']}")
                    print(f"  Time in Mentor's Timezone: {appt['mentor_time']}")
                elif language == "ro":
                    print(f"Utilizator: {appt['user']['name']}, Consultant: {appt['consultant']}")
                    print(f"  Ora în fusul orar al clientului: {appt['customer_time']}")
                    print(f"  Ora în fusul orar al mentorului: {appt['mentor_time']}")
                elif language == "fr":
                    print(f"Utilisateur: {appt['user']['name']}, Consultant: {appt['consultant']}")
                    print(f"  Heure dans le fuseau horaire du client: {appt['customer_time']}")
                    print(f"  Heure dans le fuseau horaire du mentor: {appt['mentor_time']}")
                print("-" * 40)

        except KeyboardInterrupt:
            if language == "en":
                print("\nProgram interrupted by user. Exiting gracefully.")
            elif language == "ro":
                print("\nProgramul a fost întrerupt de utilizator. Ieșire în siguranță.")
            elif language == "fr":
                print("\nProgramme interrompu par l'utilisateur. Fermeture en douceur.")

    # Method to delete an appointment
    def delete_appointment(self, language):
        try:
            # Fetch all appointments from the database
            appointments = db_list_appointments()
            if not appointments:
                if language == "en":
                    print("No appointments found to delete.")
                elif language == "ro":
                    print("Nu există programări de șters.")
                elif language == "fr":
                    print("Aucun rendez-vous à supprimer.")
                return

            # List all appointments
            if language == "en":
                print("Scheduled Appointments:")
            elif language == "ro":
                print("Programări programate:")
            elif language == "fr":
                print("Rendez-vous planifiés:")

            for idx, appt in enumerate(appointments, 1):
                if language == "en":
                    print(f"{idx}. User: {appt['user']['name']}, Consultant: {appt['consultant']}")
                    print(f"   Time in Customer's Timezone: {appt['customer_time']}")
                    print(f"   Time in Mentor's Timezone: {appt['mentor_time']}")
                elif language == "ro":
                    print(f"{idx}. Utilizator: {appt['user']['name']}, Consultant: {appt['consultant']}")
                    print(f"   Ora în fusul orar al clientului: {appt['customer_time']}")
                    print(f"   Ora în fusul orar al mentorului: {appt['mentor_time']}")
                elif language == "fr":
                    print(f"{idx}. Utilisateur: {appt['user']['name']}, Consultant: {appt['consultant']}")
                    print(f"   Heure dans le fuseau horaire du client: {appt['customer_time']}")
                    print(f"   Heure dans le fuseau horaire du mentor: {appt['mentor_time']}")

            # Prompt user to select an appointment to delete
            while True:
                try:
                    if language == "en":
                        choice = int(input("Enter the number of the appointment to delete: ")) - 1
                    elif language == "ro":
                        choice = int(input("Introduceți numărul programării de șters: ")) - 1
                    elif language == "fr":
                        choice = int(input("Entrez le numéro du rendez-vous à supprimer : ")) - 1

                    if choice < 0 or choice >= len(appointments):
                        raise ValueError("Invalid choice.")
                    break
                except ValueError:
                    if language == "en":
                        print("Invalid choice. Please try again.")
                    elif language == "ro":
                        print("Opțiune invalidă. Vă rugăm să încercați din nou.")
                    elif language == "fr":
                        print("Choix invalide. Veuillez réessayer.")

            # Remove the selected appointment
            selected_appointment = appointments[choice]
            appointments_table.remove(doc_ids=[selected_appointment.doc_id])  # Delete from the database

            if language == "en":
                print("Appointment deleted successfully.")
            elif language == "ro":
                print("Programarea a fost ștearsă cu succes.")
            elif language == "fr":
                print("Le rendez-vous a été supprimé avec succès.")

        except KeyboardInterrupt:
            if language == "en":
                print("\nOperation interrupted by user. Exiting gracefully.")
            elif language == "ro":
                print("\nOperațiunea a fost întreruptă de utilizator. Ieșire în siguranță.")
            elif language == "fr":
                print("\nOpération interrompue par l'utilisateur. Fermeture en douceur.")

