import streamlit as st
from agente import responder

st.set_page_config(page_title="Agente Financeiro", layout="centered")

st.title("💳 Assistente de Fatura de Cartão")

st.write("Faça perguntas sobre sua fatura.")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    resposta = responder(pergunta)
    st.markdown("### Resposta:")
    st.write(resposta)
