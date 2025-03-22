import random

# Lista de preguntas con sus respuestas
questions = [
    {
        "question": "¿Cuál es el lenguaje de programación usado en este proyecto?",
        "options": ["C++", "Java", "Python", "JavaScript"],
        "correct": 2  # Índice de la respuesta correcta (Python)
    },
    {
        "question": "¿Qué método en Python se usa para leer un archivo?",
        "options": ["read()", "open()", "load()", "write()"],
        "correct": 0  # Índice de la respuesta correcta (read())
    },
    {
        "question": "¿Qué biblioteca usamos para cifrar contraseñas?",
        "options": ["bcrypt", "hashlib", "crypto", "securepass"],
        "correct": 0  # Índice de la respuesta correcta (bcrypt)
    }
]

# Función para cargar una pregunta aleatoria
def start_quiz():
    question = random.choice(questions)  # Elegir una pregunta al azar
    print("\n❓", question["question"])
    
    for i, option in enumerate(question["options"]):
        print(f"{i + 1}. {option}")

    try:
        answer = int(input("👉 Tu respuesta (1-4): ")) - 1
        if answer == question["correct"]:
            print("✅ ¡Correcto!")
            return True
        else:
            print("❌ Incorrecto. La respuesta correcta era:", question["options"][question["correct"]])
            return False
    except ValueError:
        print("⚠ Entrada no válida. Debes ingresar un número entre 1 y 4.")
        return False
