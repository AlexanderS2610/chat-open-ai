from pathlib import Path
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

# Solicitud para generar texto a voz
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="este es un texto de prueba para convertir a voz, puedes escribir lo que quieras y se convertirá a audio.",
)

# Guardar manualmente el contenido en un archivo
with open("output2.mp3", "wb") as output_file:
    output_file.write(response.content)

print("Archivo de audio guardado como output2.mp3")

#https://platform.openai.com/docs/guides/audio?lang=python&audio-generation-quickstart-example=audio-out