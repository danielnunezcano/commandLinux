import sys
import subprocess
import Menu
import Generate

if __name__ == "__main__":
    command_linux=Generate.generate_linux_command(sys.argv[1])
    print("Comando a ejecutar: "+command_linux)
    menu_choice=Menu.get_user_choice()
    if menu_choice == "descripción":
        description_command=Generate.generate_command_description(command_linux)
        print(f"\033[32mDescripción:\033[0m\n{description_command}")
        menu_choice=Menu.get_user_choice_command()
    if menu_choice == "ejecutar":
        command_result = subprocess.run(command_linux, capture_output=True, shell=True, text=True)
        print(f"\033[32mResultado:\033[0m\n{command_result.stdout}")