import sys
import inquirer

def get_user_choice():
    message = "¿Quieres ver la descripción o ejecutar el comando?"
    choices = ['descripción', 'ejecutar', 'nada']
    return default_menu(message, choices)

def get_user_choice_command():
    message = "¿Quieres ejecutar el comando?"
    choices = ['ejecutar', 'nada']
    return default_menu(message, choices)

def default_menu(message, choices):
    if not sys.stdin.isatty():
        print("No se puede mostrar el menú interactivo porque no hay una terminal disponible.")
        return choices[0]  # Devolver una opción por defecto

    # Opciones del menú
    questions = [
        inquirer.List(
            'result',  # El valor seleccionado se almacenará aquí
            message=message,
            choices=choices
        )
    ]
    answer = inquirer.prompt(questions)
    return answer['result']
