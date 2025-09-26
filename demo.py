#1. Primeiro App
import streamlit as st

st.title("Exemplo de uso do Streamlit! 🚀")
st.subheader("Meu primeiro aplicativo web com Python")

st.write("Este é um app simples feito em **Streamlit**.")

nome = st.text_input("Digite seu nome:")
if nome:
    st.success(f"Bem-vindo(a), {nome}!")

#2. Widgets Interativos

st.title("Explorando Widgets")

# Slider
numero = st.slider("Qual sua idade? ", 1, 200, 25)
st.write("Você tem:", numero, "anos")

# Botão
if st.button("Clique para celebrar!"):
    st.balloons()

# Caixa de seleção
check = st.checkbox("Mostrar mensagem secreta")
if check:
    st.info("🎉 Você descobriu a mensagem secreta!")

# Lista suspensa
opcao = st.selectbox("Escolha uma linguagem de programação",
                     ["Python", "Java", "C", "JavaScript"])
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

import requests

st.title("📚 Busca de Livros por ISBN")
st.write("Digite o ISBN de um livro para buscar informações na API da Open Library.")

# Entrada do usuário
isbn = st.text_input("Informe o ISBN (ex: 9780140328721):")

if isbn:
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    response = requests.get(url)

    if response.status_code == 200:
        livro = response.json()
        
        st.subheader("📖 Informações do Livro")
        st.write("**Título:**", livro.get("title", "Não encontrado"))
        st.write("**Número de páginas:**", livro.get("number_of_pages", "Não informado"))
        st.write("**Publicado em:**", livro.get("publish_date", "Não informado"))

        # Tenta buscar autores
        if "authors" in livro:
            autores = []
            for autor in livro["authors"]:
                autor_url = f"https://openlibrary.org{autor['key']}.json"
                autor_resp = requests.get(autor_url)
                if autor_resp.status_code == 200:
                    autor_data = autor_resp.json()
                    autores.append(autor_data.get("name", "Desconhecido"))
            st.write("**Autor(es):**", ", ".join(autores))
    else:
        st.error("Livro não encontrado. Verifique o ISBN.")

import streamlit as st
import requests
import pandas as pd

st.title("☀️ Previsão do Tempo - Open Meteo API")

st.write("Digite o nome de uma cidade para ver a previsão do tempo.")

#App forecast
# Entrada do usuário
cidade = st.text_input("Cidade:", "São Paulo")

if cidade:
    # 1. Obter latitude/longitude da cidade (API Nominatim / OpenStreetMap)
    url_geo = f"https://nominatim.openstreetmap.org/search?city={cidade}&format=json"
    headers = {"User-Agent": "streamlit-app/1.0 (contato@exemplo.com)"}

    resp = requests.get(url_geo, headers=headers)

    if resp.status_code == 200:
        geo_resp = resp.json()
        if geo_resp:
            lat = geo_resp[0]["lat"]
            lon = geo_resp[0]["lon"]

            # 2. Consultar previsão do tempo (próximos 5 dias, de hora em hora)
            url_clima = (
                f"https://api.open-meteo.com/v1/forecast?"
                f"latitude={lat}&longitude={lon}"
                f"&hourly=temperature_2m"
                f"&forecast_days=5"
                f"&timezone=auto"
            )
            clima_resp = requests.get(url_clima).json()

            if "hourly" in clima_resp:
                # Dados atuais
                st.subheader(f"🌍 Clima em {cidade}")
                st.write("Latitude:", lat, "Longitude:", lon)

                # Criar DataFrame com previsão
                df = pd.DataFrame({
                    "Hora": clima_resp["hourly"]["time"],
                    "Temperatura (°C)": clima_resp["hourly"]["temperature_2m"]
                })

                # Mostrar tabela
                st.write("📅 Previsão Horária")
                st.dataframe(df.head(24))  # mostra só o 1º dia

                # Gráfico
                st.subheader("📊 Gráfico de Temperatura (Próximos 5 dias)")
                st.line_chart(df.set_index("Hora"))

            else:
                st.error("Não foi possível obter a previsão.")
        else:
            st.error("Cidade não encontrada. Verifique o nome digitado.")
    else:
        st.error("Erro ao consultar serviço de geolocalização.")





