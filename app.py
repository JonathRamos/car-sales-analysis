import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')  # Lee el archivo CSV

# Título de la aplicación
st.header('Análisis de Anuncios de Venta de Coches')

# Mostrar las primeras filas del conjunto de datos
st.subheader('Vista previa de los datos')
st.write(car_data.head())  # Muestra las primeras 5 filas de la tabla

# Botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Si se hace clic en el botón
    st.write('Creando un histograma para la columna odómetro...')
    # Crear histograma para la columna 'odometer'
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)  # Mostrar el gráfico

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # Si se hace clic en el botón
    st.write('Creando un gráfico de dispersión...')
    fig = px.scatter(car_data, x="price", y="odometer",
                     color="model")  # Usando 'model' como color
    st.plotly_chart(fig, use_container_width=True)  # Mostrar el gráfico
