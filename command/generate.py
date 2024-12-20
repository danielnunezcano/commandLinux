import custom_gemini

def generate_command(request,so):
    question_to_gemini = f"Dame la instrucción para terminal de {so} de lo siguiente, no me des explicaciones, solo quiero el comando y que sea en en texto plano:"
    return custom_gemini.generate_clean_response(question_to_gemini,request)

def generate_command_description(request,so):
    question_to_gemini = f"Dime la descripción del siguente comando de {so}:"
    return custom_gemini.generate_clean_response(question_to_gemini,request)
