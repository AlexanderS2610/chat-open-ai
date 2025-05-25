import os
from openai import OpenAI #pip install openai se hace con la version openai-1.42.0
from dotenv import load_dotenv

# Cargar las variables de entorno con dotenv
load_dotenv()

# Clave de API de OpenAI desde el entorno
openai_key = os.getenv('ai_key')
# Reemplaza 'tu-api-key' con tu clave de API de OpenAI
#openai_key = "sk-proj"
#org_ID ="" #Si se tiene se ingresa


client = OpenAI(
    # This is the default and can be omitted
    api_key=openai_key
)

def obtener_respuesta(messages):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=50,  # Ajusta el límite de tokens según tus necesidades
        temperature=0.7,  # Ajusta la creatividad de la respuesta
        top_p=1    
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    # Definir el mensaje inicial del sistema
    messages = [
        {"role": "system", "content": "Eres un contador de chistes."}
    ]
    
    while True:
        prompt = input("Escribe tu pregunta (o 'salir' para terminar): ")
        
        if prompt.lower() == 'salir':
            print("¡Hasta luego!")
            break

        # Agregar el mensaje del usuario a la conversación
        messages.append({"role": "user", "content": prompt})

        # Obtener la respuesta del asistente
        respuesta = obtener_respuesta(messages)

        # Agregar la respuesta del asistente a la conversación
        messages.append({"role": "assistant", "content": respuesta})

        # Mostrar la respuesta al usuario
        print("GPT-4 dice:", respuesta)