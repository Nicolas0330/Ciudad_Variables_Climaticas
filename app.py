import streamlit as st
from PIL import Image

st.title("Aplicaciones para Ciudades Inteligentes y Sostenibles")

st.header("En este espacio podras obtener informacion sobre variables climaticas en ciudades alrededor del mundo")

image = Image.open('Clima.jpg')
st.image(image, caption='Inteligencia Urbana')
st.write("Enlace para mi sistema de internet de las cosas")
st.write("Ingresa al link [link] (http://demo.thingsboard.io/dashboards/9a61e170-565c-11ee-b6bf-f9525dc44ab3)")
