import streamlit as st
import pandas as pd
import numpy as np

# Titulo
st.title ("Futdados")

#Sidebar
st.sidebar.header("Ligas")
liga_selecionada = st.sidebar.selectbox("Selecione a liga", ["Alemanha", "Inglaterra", "Espanha", "Itália", "França"])

st.sidebar.header("Temporadas")
temporada_selecionada = st.sidebar.selectbox("Selecione a temporada", ["2022/2023", "2023/2024", "2024/2025"])

#Web scraping
def carregar_dados(liga, temporada):

    if liga_selecionada == "Alemanha":
        liga = "D1"
    if liga_selecionada == "Inglaterra":
        liga = "E0"
    if liga_selecionada == "Espanha":
        liga = "SP1"
    if liga_selecionada == "Itália":
        liga = "I1"
    if liga_selecionada == "França":
        liga = "F1"

    if temporada_selecionada == "2022/2023":
        temporada = "2223"
    if temporada_selecionada == "2023/2024":
        temporada = "2324"
    if temporada_selecionada == "2024/2025":
        temporada = "2425"

    url = f"https://www.football-data.co.uk/mmz4281/"+temporada+"/"+liga+".csv"
    data = pd.read_csv(url)
    return data

df = carregar_dados(liga_selecionada, temporada_selecionada)

st.subheader("Dados Carregados: "+liga_selecionada)
st.dataframe(df)