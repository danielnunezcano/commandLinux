import google.generativeai as genai
import os
import sys
import subprocess

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-pro')
request = sys.argv[1]
questionToGemini = "Dame la instrucción para terminal de linux de lo siguiente, no me des explicaciones, solo quiero el comando y que sea en en texto plano: " + request

response = model.generate_content(questionToGemini)
responseGemini = response.text.rstrip()
# Ejecuta el comando "ls -lh" y guarda la salida en la variable resultado
resultado = subprocess.run(responseGemini, capture_output=True, shell=True, text=True)

# Imprime la salida estándar del comando
print("Comando ejecutado: "+responseGemini)
print("¿Quieres ejecutarlo? (S/n)")
user_input = input()
if user_input == "S" or user_input == "s" :
    print("Resultado:")
    print(resultado.stdout)
else:
    print("No se ejecuta")
