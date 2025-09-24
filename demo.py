#1. Primeiro App
import streamlit as st

st.title("Olá, Streamlit! 🚀")
st.subheader("Meu primeiro aplicativo web com Python")

st.write("Este é um app simples feito em **Streamlit**.")

nome = st.text_input("Digite seu nome:")
if nome:
    st.success(f"Bem-vindo(a), {nome}!")

#2. Widgets Interativos

st.title("Explorando Widgets")

# Slider
numero = st.slider("Escolha um número", 1, 100, 25)
st.write("Você escolheu:", numero)

# Botão
if st.button("Clique para celebrar!"):
    st.balloons()

# Caixa de seleção
check = st.checkbox("Mostrar mensagem secreta")
if check:
    st.info("🎉 Você descobriu a mensagem secreta!")

# Lista suspensa
opcao = st.selectbox("Escolha uma linguagem de programação",
                     ["Python", "Java", "C++", "JavaScript"])
st.write("Você escolheu:", opcao)

#3. Visualização de Dados Aleatórios

import pandas as pd
import numpy as np

st.title("Visualização de Dados")

# Criar DataFrame aleatório
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.write("Tabela de dados aleatórios:")
st.dataframe(df)

# Gráficos
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

#4. Upload de Arquivo

import streamlit as st
import pandas as pd

st.title("Upload de Arquivo CSV")

uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Pré-visualização dos dados:")
    st.dataframe(df.head())

    st.write("Descrição estatística:")
    st.write(df.describe())

#5. Mini Dashboard com o Iris Dataset

import seaborn as sns

st.title("Dashboard - Conjunto de Dados Iris 🌸")

# Carregar dataset
df = sns.load_dataset("iris")

# Mostrar dados
st.subheader("Dados da Tabela")
st.dataframe(df)

# Filtro por espécie
especie = st.selectbox("Selecione a espécie", df["species"].unique())
df_filtrado = df[df["species"] == especie]

st.write(f"Mostrando apenas dados da espécie: **{especie}**")
st.dataframe(df_filtrado)

# Gráficos
st.subheader("Distribuição do Comprimento da Sépala")
st.bar_chart(df_filtrado["sepal_length"])

st.subheader("Dispersão: Comprimento vs Largura da Pétala")
st.scatter_chart(df_filtrado[["petal_length", "petal_width"]])

