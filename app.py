import streamlit as st 
import pandas as pd
import plotly.express as pe 

st.header('Ventas de Vehiculos') #crea encabezado

data = pd.read_csv('/Users/EVILLALONA/Phyton Basico/Proyecto Sprint 5/my_proyect/notebooks/vehicles_us.csv') # lee el conjunto de datos
boton_h = st.button('Contruye Histograma') # crea un boton para histograma
boton_d = st.button('Contruye Grafico Dispersion') # crea un boton para grafico dispersion

if boton_h:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches') 

    #crear histograma
    fig = pe.histogram(data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

if boton_d:
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

    fig = pe.scatter(data, x="model", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True) 


