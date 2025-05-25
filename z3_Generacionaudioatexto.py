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

audio_file = open("Grabación.m4a", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)

print(transcription.text)

#https://platform.openai.com/docs/guides/speech-to-text