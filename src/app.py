import streamlit as st
import json
from agente import responder

st.set_page_config(page_title="Agente Financeiro", layout="centered")

st.title("💳 Assistente de Fatura de Cartão")

st.write("Envie sua fatura em JSON ou utilize a fatura padrão.")

uploaded_file = st.file_uploader(
    "Envie sua fatura (.json)",
    type=["json"]
)

fatura = None

# =========================
# INPUT
# =========================

if uploaded_file is None:
    with open("data/fatura_cartao.json") as f:
        fatura = json.load(f)
    st.info("📄 Usando fatura padrão")

else:
    try:
        fatura = json.load(uploaded_file)
        st.success("📂 Fatura JSON carregada com sucesso!")
    except:
        st.error("Erro ao ler o JSON enviado.")

# =========================
# OUTPUT
# =========================

if fatura:
    st.subheader("📊 Preview da Fatura")
    st.json(fatura)

    st.subheader("💬 Faça sua pergunta")

    pergunta = st.text_input("Digite sua pergunta:")

    if pergunta:
        resposta = responder(pergunta, fatura)
        st.markdown("### Resposta:")
        st.write(resposta)