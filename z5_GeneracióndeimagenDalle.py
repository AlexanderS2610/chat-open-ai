from openai import OpenAI

# Generar una imagen

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

response = client.images.generate(
    model="dall-e-3",
    prompt="un perro con un hueso",
    size="1024x1024",
    quality="standard",
    n=1,
)

print(response.data[0].url)

# https://platform.openai.com/docs/guides/images?context=python