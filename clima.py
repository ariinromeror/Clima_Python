import streamlit as st
import urllib.request
import json

st.set_page_config(page_title="App Clima", page_icon="🌦️")
st.title("App Clima")

ciudad = st.text_input("Escribe el nombre de una ciudad:")
api_key = "0fabd4bf8af750d1ffabedbaa084eac3"

if st.button("Consultar"):
    if ciudad:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
        try:
            with urllib.request.urlopen(url) as respuesta:
                datos = json.loads(respuesta.read().decode())
                
                temp = datos['main']['temp']
                humedad = datos['main']['humidity']
                desc = datos['weather'][0]['description']

                st.success(f"Resultados para {ciudad.capitalize()}")
                st.metric("Temperatura", f"{temp} °C")
                st.write(f"Estado: {desc.capitalize()} | Humedad: {humedad}%")
        except Exception:
            st.error("No se encontró la ciudad o hay un error de conexión.")