import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')  # leer los datos
# Encabezado
st.title("Análisis de datos de vehículos en EU")
# Primer botón - Histograma
st.header("Histograma de kilometraje")
hist_button = st.button('Construir histograma')
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Segundo botón - Gráfico de dispersión
st.header("Dispersión tipo de auto/precio")
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(df, x="type", y="price")
    st.plotly_chart(fig, use_container_width=True)
