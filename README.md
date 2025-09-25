Perfeito, Leonardo! 😄 Vou criar uma **versão final do README.md** com **badges**, incluindo o link direto do seu app Streamlit Cloud.

---

# 📄 README.md (versão final com badges)

````markdown
# 🌟 Streamlit Demo - Projeto Completo

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-orange)](https://streamlit.io/)
[![Open in Streamlit](https://img.shields.io/badge/Open%20App-Streamlit-blue)](https://testeapp-pwaaj6qwgna38ekkhkaefo.streamlit.app/)

Este projeto é um **exemplo completo de aplicativos web com Streamlit**, demonstrando:

- Widgets interativos
- Visualização de dados
- Upload de arquivos CSV
- Dashboards simples
- Consumo de APIs públicas (Open Library, Open-Meteo)

---

## 🚀 Funcionalidades

1. **Primeiro App**
   - Título, subtítulo e entrada de nome com feedback interativo.

2. **Widgets Interativos**
   - Slider, botão, checkbox e selectbox.

3. **Visualização de Dados Aleatórios**
   - Criação de DataFrame com dados aleatórios.
   - Gráficos: linha, barra e área.

4. **Upload de Arquivo CSV**
   - Pré-visualização e estatísticas do CSV.

5. **Mini Dashboard com Iris Dataset**
   - Filtro por espécie e gráficos interativos.

6. **Busca de Livros por ISBN**
   - API Open Library: título, autor(es), páginas, data de publicação.

7. **Previsão do Tempo**
   - APIs Nominatim e Open-Meteo: previsão horária e gráficos.

---

## 🛠 Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- Pandas
- Numpy
- Seaborn
- Requests
- Matplotlib (opcional)

---

## 💾 Instalação Local

1. Clone o repositório:
```bash
git clone https://github.com/proflgrando/StreamlitDemo.git
cd StreamlitDemo
````

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Rode localmente:

```bash
streamlit run demo.py
```

---

## ☁️ Deploy no Streamlit Cloud

1. Faça login no [Streamlit Cloud](https://streamlit.io/cloud).
2. Clique em **“New app” → “Deploy from GitHub”**.
3. Selecione o repositório: [`proflgrando/StreamlitDemo`](https://github.com/proflgrando/StreamlitDemo) e a branch desejada.
4. Clique em **Deploy**. O app estará online automaticamente.
5. Acesse o app aqui: [Abrir App](https://testeapp-pwaaj6qwgna38ekkhkaefo.streamlit.app/)

---

## 📂 Estrutura do Projeto

```
StreamlitDemo/
├─ demo.py               # arquivo principal do Streamlit
├─ requirements.txt      # dependências Python
├─ .streamlit/           # pasta opcional para configs do Streamlit
├─ data/                 # pasta para CSVs ou datasets
├─ README.md             # documentação
```

---

## 🔑 Boas Práticas

* Teste localmente antes do deploy.
* Mantenha `requirements.txt` atualizado para evitar conflitos.

---

## 📚 Referências

* [Streamlit Docs](https://docs.streamlit.io/)
* [Pandas Docs](https://pandas.pydata.org/docs/)
* [Seaborn Docs](https://seaborn.pydata.org/)
* [Requests Docs](https://docs.python-requests.org/)
* [Open Library API](https://openlibrary.org/developers/api)
* [Open-Meteo API](https://open-meteo.com/)

````

---

# 📄 requirements.txt

```text
streamlit
pandas
numpy
seaborn
requests
matplotlib
````

