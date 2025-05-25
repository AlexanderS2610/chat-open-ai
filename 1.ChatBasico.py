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

def obtener_respuesta(prompt):

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "eres un contador de chistes."},
            {
                "role": "user", "content": prompt
            }
        ],
        max_tokens=50,  # Ajusta el límite de tokens según tus necesidades
        temperature=0.7,  # Ajusta la creatividad de la respuesta
        top_p=1    
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    prompt = input("Escribe tu pregunta: ")
    respuesta = obtener_respuesta(prompt)
    print("GPT-4 dice:", respuesta)

    #print(completion.choices[0].message)