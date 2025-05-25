from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar las variables de entorno con dotenv
load_dotenv()

# Clave de API de OpenAI desde el entorno
openai_key = os.getenv('ai_key')

# Reemplaza 'tu-api-key' con tu clave de API de OpenAI
#openai_key = "sk-proj"
#org_ID ="" #Si se tiene se ingresa

client = OpenAI(
    api_key=openai_key
)

######Codigo para chat

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Cual es la historia de chat gpt"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
