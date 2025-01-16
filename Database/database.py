from tinydb import TinyDB, Query
import os

# Get the base directory dynamically relative to the script's location
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # One level up from the current script
DB_PATH = os.path.join(BASE_DIR, 'db.json')  # Database file path

# Initialize the database
db = TinyDB(DB_PATH)

# Tabele pentru utilizatori și programări
users_table = db.table('users')
appointments_table = db.table('appointments')

# Verificare unicitate utilizator (după nume)
def is_user_name_unique(name):
    User = Query()
    return not users_table.search(User.name == name)

# Adăugare utilizator
def add_user(user_id, name, timezone):
    if not is_user_name_unique(name):
        return f"User with name '{name}' already exists!"

    # Găsește următorul ID disponibil
    existing_users = users_table.all()
    if not existing_users:
        user_id = 1  # Începe de la 1
    else:
        user_id = max(user['user_id'] for user in existing_users) + 1

    users_table.insert({'user_id': user_id, 'name': name, 'timezone': timezone})
    return "User added successfully!"


# Ștergere utilizator
def delete_user(name):
    User = Query()
    if not is_user_name_unique(name):  # Asigurăm că utilizatorul există
        users_table.remove(User.name == name)
        return "User deleted successfully!"
    return f"User with name '{name}' does not exist."

# Listare utilizatori
def list_users():
    data = users_table.all()  # Accesează toate înregistrările din tabelul 'users_table'
    print("Debug: Users in database:", data)  # Verifică ce date sunt returnate
    return data

# Adăugare programare
def add_appointment(user, consultant, customer_time, mentor_time):
    appointments_table.insert({
        'user': user,
        'consultant': consultant,
        'customer_time': customer_time,
        'mentor_time': mentor_time
    })
    return "Appointment added successfully!"

# Listare programări
def list_appointments():
    return appointments_table.all()