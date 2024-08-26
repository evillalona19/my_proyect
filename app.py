import streamlit as st 
import pandas as pd
import plotly.express as pe 

st.header('Panel de Control Ventas de Vehiculos') #crea encabezado

data = pd.read_csv('notebooks/vehicles_us.csv') # lee el conjunto de datos
boton_h = st.checkbox('Construye Histograma') # crea un boton para histograma
boton_d = st.checkbox('Construye Grafico Dispersion') # crea un boton para grafico dispersion

if boton_h:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches') 

    #crear histograma
    fig = pe.histogram(data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

if boton_d:
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

    fig = pe.scatter(data, x="model", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True) 


