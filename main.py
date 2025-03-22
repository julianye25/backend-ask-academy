from core.auth import register

if __name__ == "__main__":
    while True:
        action = input(
            "\n¿Quieres [r]egistrar, [i]niciar sesión o [s]alir?: ").lower()

        if action == "r":
            user = input("Nombre de usuario: ")
            pwd = input("Contraseña: ")
            register(user, pwd)

        # elif action == "i":
        #     user = input("Nombre de usuario: ")
        #     pwd = input("Contraseña: ")
        #     login(user, pwd)

        elif action == "s":
            break

        else:
            print("⚠ Opción no válida.")
