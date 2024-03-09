import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

review = pd.read_csv("dataset/customer reviews.csv")
top100 = pd.read_csv("dataset/Top-100 Trending Books.csv")
st.write("""
# Reviews
""")
review
st.write("""
# Ranking Top 100
""")


price_max = top100["book price"].max()
price_min = top100["book price"].min()


# Define o valor padrão dentro do intervalo de preço
default_price = (price_max + price_min) / 2  # Exemplo: define para o preço médio

max_price = st.sidebar.slider("Faixa de preço", price_min, price_max, default_price)
df_books = top100[top100["book price"] <= max_price]
df_books


fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])


col1, col2 = st.columns(2)
col1.plotly_chart(fig2)
col2.plotly_chart(fig)

