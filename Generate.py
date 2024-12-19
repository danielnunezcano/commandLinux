import custom_gemini

def generate_linux_command(request):
    question_to_gemini = "Dame la instrucción para terminal de linux de lo siguiente, no me des explicaciones, solo quiero el comando y que sea en en texto plano:"
    return custom_gemini.generate_clean_response(question_to_gemini,request)

def generate_command_description(request):
    question_to_gemini = "Dime la descripción del siguente comando de linux:"
    return custom_gemini.generate_clean_response(question_to_gemini,request)
