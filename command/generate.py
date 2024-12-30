import custom_gemini

def generate_command(request,so):
    question_to_gemini = f"Dame la instrucción para terminal de {so} de lo siguiente, no me des explicaciones, solo quiero el comando y que sea en en texto plano: {request}"
    response =  custom_gemini.generate_response(question_to_gemini)
    return response.text.rstrip().replace("```", "").replace("\n", "")

def generate_command_description(request,so):
    question_to_gemini = f"Dime la descripción del siguente comando de {so}: {request}"
    return custom_gemini.generate_response(question_to_gemini).text
