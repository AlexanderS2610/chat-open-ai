import streamlit as st #streamlit==1.38.0
from openai import OpenAI #open== 1.44.0
from dotenv import load_dotenv
import os
from PIL import Image




# Titulo
st.title("💬 Chatbot")
st.write(
    "Escribe cualquier duda y el chat te respondera"
)

    #Api Key de Openai
openai_key = os.getenv('ai_key')

    #Crear un cliente OpenAI.
client = OpenAI(
        api_key=openai_key)

    # Cree una variable de estado de sesión para almacenar los mensajes de chat. Esto asegura que el
    # mensajes persisten en las repeticiones.
if "messages" not in st.session_state:
    st.session_state.messages = []

    # Mostrar los mensajes de chat existentes a través de `st.chat_message`
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
         st.markdown(message["content"])

    # Cree un campo de entrada de chat para permitir al usuario ingresar un mensaje. Esto mostrará
    # automáticamente en la parte inferior de la página.

if prompt := st.chat_input("What is up?"):

        # Almacenar y mostrar el mensaje actual.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
         st.markdown(prompt)

        # Generar una respuesta usando la API OpenAI.
    stream = client.chat.completions.create(
         model="gpt-4o-mini",
         messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
            ],
            stream=True,
        )

        # Transmita la respuesta al chat usando `st.write_stream`, luego guárdela

    with st.chat_message("assistant"):
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})