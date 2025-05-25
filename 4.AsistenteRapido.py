#Se instala las librerias 
#pip install openai se hace con la version openai-1.42.0
#pip install cohere tiktoken openai >> null

from pprint import pprint #Paquete para mostrar bonito los datos
import json #modulo json para trabajar con datos en formato json
import os
import openai #paquete de openai para colab
from openai import OpenAI
import time
from dotenv import load_dotenv

# Cargar las variables de entorno con dotenv
load_dotenv()

# Clave de API de OpenAI desde el entorno
openai_key = os.getenv('ai_key')

# Reemplaza 'tu-api-key' con tu clave de API de OpenAI
#openai_key = "sk-proj"
#org_ID ="" #Si se tiene se ingresa

#Crear el cliente de openai
client = OpenAI(
    # This is the default and can be omitted
    api_key=openai_key
)

#Crear un asistente
#time.sleep(5)
assistant = client.beta.assistants.create(
  name="Math Tutor",
  instructions="Eres un tutor personal de matemáticas. Escribe y ejecuta código para responder preguntas de matemáticas.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-3.5-turbo-1106",
)
print("este es el id del asistente",assistant.id)


#Crear un hilo
#time.sleep(2)
thread = client.beta.threads.create()
print("este es el id del hilo creado",thread.id)
print("este es el id del hilo creado",thread)

#Agregar un mensaje el hilo
#time.sleep(1)
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="Necesito resolver la ecuación `3x + 11 = 14`, cuando se tenga el resultado multiplicarlo por 12 y dividirlo en 3. ¿Me puedes ayudar?"
)
print(message)


#Crear una carrera
#time.sleep(5)
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Diríjase al usuario como Jane Doe. El usuario tiene una cuenta premium."
)
print("Este es el id de lo que se ejecuto", run.id)


# Verificar el estatus del 'run'
while True:
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    print("este es el estatus de lo ejecutado", run.status)

    # Si el estado es 'completed', se continúa con la ejecución del siguiente paso
    if run.status == "completed":
        break
    
    # Esperar 5 segundos antes de volver a comprobar
    time.sleep(5)

# Ejecución del siguiente paso una vez que el estado es 'completed'
# Recuperar los mensajes de la ejecución
messages = client.beta.threads.messages.list(
    thread_id=thread.id
)
print("se ejecuta el mensaje codificado", messages)

# Imprimir todos los mensajes que se han ejecutado hasta ahora
for message in reversed(messages.data):
    print(message.role + ": " + message.content[0].text.value)

#borrar el asistente
delete=client.beta.assistants.delete(assistant.id)
print(delete)
