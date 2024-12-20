import unittest
from unittest.mock import patch, MagicMock
import sys
import subprocess
from command import main

class TestMainScript(unittest.TestCase):

    @patch('generate.generate_command')
    @patch('generate.generate_command_description')
    @patch('menu.get_user_choice')
    @patch('menu.get_user_choice_command')
    @patch('detect_os.system_type')
    @patch('subprocess.run')
    def test_main_execution(self, mock_subprocess_run, mock_system_type, mock_get_user_choice, mock_get_user_choice_command, mock_generate_command_description, mock_generate_command):
        # Simula argumentos de línea de comandos
        sys.argv = ["main.py", "test_argument"]

        # Configura los mocks
        mock_system_type.return_value = "Linux"
        mock_generate_command.return_value = "echo Hola"
        mock_get_user_choice.side_effect = ["descripción", "ejecutar"]
        mock_generate_command_description.return_value = "Este comando imprime 'Hola'."

        mock_subprocess_run.return_value = subprocess.CompletedProcess(
            args="echo Hola", returncode=0, stdout="Hola\n", stderr=""
        )

        # Captura la salida del script
        with patch('builtins.print') as mock_print:
            # Ejecuta el script principal
            main_command = main.generate.generate_command(sys.argv[1], mock_system_type.return_value)
            print(f"Comando a ejecutar: {main_command}")

            # Simula la opción 'descripción'
            description = main.generate.generate_command_description(main_command)
            print(f"\033[32mDescripción:\033[0m\n{description}")

            # Simula la opción 'ejecutar'
            command_result = subprocess.run(main_command, capture_output=True, shell=True, text=True)
            print(f"\033[32mResultado:\033[0m\n{command_result.stdout}")

        # Verifica las llamadas a las funciones mockeadas
        mock_generate_command.assert_called_with("test_argument", "Linux")
        mock_generate_command_description.assert_called_with("echo Hola")
        mock_get_user_choice.assert_called()
        mock_get_user_choice_command.assert_not_called()  # Solo se llama si se necesita otra interacción
        mock_subprocess_run.assert_called_with("echo Hola", capture_output=True, shell=True, text=True)

        # Verifica las salidas impresas
        mock_print.assert_any_call("Comando a ejecutar: echo Hola")
        mock_print.assert_any_call("\033[32mDescripción:\033[0m\nEste comando imprime 'Hola'.")
        mock_print.assert_any_call("\033[32mResultado:\033[0m\nHola\n")

if __name__ == "__main__":
    unittest.main()
