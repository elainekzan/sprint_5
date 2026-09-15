import streamlit as st
import pandas as pd
import plotly.express as px

# Ler os dados
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho do aplicativo
st.header('Análise de anúncios de vendas de carros')

# Botão para criar histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    fig = px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, use_container_width=True)


# Botão para criar gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão entre quilometragem e preço')

    fig = px.scatter(car_data, x='odometer', y='price')

    st.plotly_chart(fig, use_container_width=True)