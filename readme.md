## Processo de Implementação de um Dashboard Interativo com Streamlit

**Introdução:**

Este README descreve o processo de criação de um dashboard interativo com Streamlit, utilizando Python. O dashboard demonstra a análise de dados de livros, incluindo:

* **Exibição de resenhas de clientes**
* **Ranking dos 100 livros mais vendidos**
* **Filtragem por faixa de preço**
* **Visualização da distribuição de publicações por ano**

**Requisitos:**

* Python 3.x
* Streamlit
* Pandas
* Plotly Express

**Etapas:**

1. **Instalação de Bibliotecas:**

```
pip install streamlit pandas plotly-express
```

2. **Importação de Bibliotecas:**

```python
import streamlit as st
import pandas as pd
import plotly.express as px
```

3. **Carregamento de Dados:**

```python
review = pd.read_csv("dataset/customer reviews.csv")
top100 = pd.read_csv("dataset/Top-100 Trending Books.csv")
```

4. **Exibição de Resenhas e Ranking:**

```python
st.write("""
# Reviews
""")
review

st.write("""
# Ranking Top 100
""")
top100
```

5. **Filtro por Faixa de Preço:**

```python
price_max = top100["book price"].max()
price_min = top100["book price"].min()

default_price = (price_max + price_min) / 2

max_price = st.sidebar.slider("Faixa de preço", price_min, price_max, default_price)
df_books = top100[top100["book price"] <= max_price]

st.write(df_books)
```

6. **Visualização da Distribuição de Publicações:**

```python
fig = px.bar(df_books["year of publication"].value_counts())

st.plotly_chart(fig)
```

7. **Execução do Script:**

```
python main.py
```

**Observações:**

* Este é um exemplo básico. Você pode adicionar mais funcionalidades e personalizações.
* O código foi testado com Python 3.8 e Streamlit 1.14.0.
* Certifique-se de ter os dados (`customer reviews.csv` e `Top-100 Trending Books.csv`) na mesma pasta do script.

**Recursos Adicionais:**

* Documentação do Streamlit: [https://docs.streamlit.io/](https://docs.streamlit.io/)
* Tutoriais do Streamlit: [URL inválido removido]
* Documentação do Plotly Express: [URL inválido removido]

**Espero que este README seja útil!**

