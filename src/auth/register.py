import json
import hashlib
import os

FILE_PATH = "src/db/users.json"


def load_users():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_users(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def register(username, password):
    users_data = load_users()
    if user in users_data:
        print("El usuario ya existe.")
        return False

    hashed_password = hashlib.sha256(password.encode())
    users_data["users"].append(
        {"username": username, "password": hashed_password.hexdigest()})
    save_users(users_data)
    print("Usuario registrado correctamente.")


if __name__ == "__main__":
    while True:
        action = input(
            "\n¿Quieres [r]egistrar, [i]niciar sesión o [s]alir?: ").lower()

        if action == "r":
            user = input("Nombre de usuario: ")
            pwd = input("Contraseña: ")
            register(user, pwd)

        elif action == "i":
            user = input("Nombre de usuario: ")
            pwd = input("Contraseña: ")
            login(user, pwd)

        elif action == "s":
            break

        else:
            print("⚠ Opción no válida.")
