import sys
import subprocess
import menu
import generate
import detect_os

if __name__ == "__main__":
    so=detect_os.system_type()
    command= generate.generate_command(sys.argv[1],so)
    print("Comando a ejecutar: "+command)
    menu_choice= menu.get_user_choice()
    if menu_choice == "descripción":
        description_command= generate.generate_command_description(command,so)
        print(f"\033[32mDescripción:\033[0m\n{description_command}")
        menu_choice= menu.get_user_choice_command()
    if menu_choice == "ejecutar":
        command_result = subprocess.run(command, capture_output=True, shell=True, text=True)
        print(f"\033[32mResultado:\033[0m\n{command_result.stdout}")