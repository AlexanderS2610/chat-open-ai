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

#Codigo de generación de Imagen
response = client.images.generate(
    prompt="un mini Perro",
    n=2,
    size="1024x1024"
)

print(response.data[0].url)