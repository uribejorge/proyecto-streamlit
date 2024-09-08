import streamlit as st
from datetime import datetime

# Título de la aplicación
st.title("Mi Primer Proyecto con Streamlit")

# Descripción
"""
### Bienvenido a la aplicación interactiva con Streamlit.

Aquí puedes ingresar tu nombre, seleccionar tu género, y elegir una fecha. ¡Todo en tiempo real!
"""

# Input para el nombre del usuario
st.subheader("1. Ingrese su nombre")
nombre = st.text_input("Escriba su nombre")

# Selector de género
st.subheader("2. Seleccione su género")
genero = st.radio("Elija una opción:", ('Masculino', 'Femenino', 'Otro'))

# Selector de fecha
st.subheader("3. Seleccione una fecha")
fecha = st.date_input("Seleccione una fecha", datetime.now())

# Botón para mostrar el resultado
if st.button('Mostrar resultado'):
    st.write(f"Hola **{nombre}**, has seleccionado el género **{genero}** y la fecha **{fecha}**.")
else:
    st.write("Completa la información y presiona el botón para ver los resultados.")

# Footer
st.markdown("### Gracias por usar esta aplicación. ¡Modifícala según lo necesites!")
