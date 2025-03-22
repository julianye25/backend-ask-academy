import json
import hashlib
import os

FILE_PATH = "db/users.json"

def load_users():
    """Carga los usuarios desde un archivo JSON"""
    if not os.path.exists(FILE_PATH):
        return {"users": []}
    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {"users": []}

def save_users(data):
    """Guarda los usuarios en el archivo JSON"""
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def register(username, password):
    """Registra un usuario"""
    users_data = load_users()
    
    for user in users_data["users"]:
        if user["username"] == username:
            print("⚠️ El usuario ya existe.")
            return False

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users_data["users"].append({"username": username, "password": hashed_password})
    save_users(users_data)
    print("✅ Usuario registrado correctamente.")
    return True

def login(username, password):
    """Inicia sesión verificando el usuario y la contraseña"""
    users_data = load_users()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    for user in users_data["users"]:
        if user["username"] == username and user["password"] == hashed_password:
            print("✅ Inicio de sesión correcto.")
            return True
    
    print("⚠️ Usuario o contraseña incorrectos.")
    return False
