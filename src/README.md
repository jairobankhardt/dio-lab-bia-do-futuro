# 💳 Assistente de Fatura de Cartão

<p align="center">
  <b>Agente financeiro inteligente para interpretar faturas de cartão de crédito com IA</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=flat&logo=streamlit">
  <img src="https://img.shields.io/badge/OpenAI-GPT-green?style=flat">
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow">
</p>

---

## 🚀 Sobre o Projeto

Este projeto implementa um **agente financeiro conversacional (Clara)** capaz de interpretar faturas de cartão de crédito e responder perguntas em linguagem natural.

A aplicação utiliza:

- 🧠 IA generativa (ChatGPT)
- 📊 Dados estruturados (JSON)
- 💬 Interface interativa (Streamlit)

---

## ✨ Funcionalidades

- Interpretação da fatura  
- Interface conversacional  
- Respostas com IA  
- Uso de dados estruturados  
- Redução de alucinação com grounding  

---

## 🗂 Estrutura do Projeto

    src/
    ├── app.py
    ├── agente.py
    ├── config.py
    └── requirements.txt

    data/
    ├── fatura_cartao.json
    └── regras_cartao.json

    .vscode/
    └── settings.json

    Makefile
    .env
    .gitignore

---

# ⚙️ Setup Completo

## 1️⃣ Criar `.gitignore`

Crie um arquivo `.gitignore` na raiz:

    .venv/
    __pycache__/
    *.pyc
    .env
    .streamlit/
    .vscode/

---

## 2️⃣ Configurar VSCode

Crie o arquivo:

    .vscode/settings.json

Conteúdo:

    {
      "python.defaultInterpreterPath": ".venv/bin/python"
    }

Isso faz o VSCode usar automaticamente o ambiente virtual.

---

## 3️⃣ Criar Makefile (automação)

Crie um arquivo `Makefile` na raiz:

    setup:
        python3 -m venv .venv
        . .venv/bin/activate && pip install -r src/requirements.txt

    run:
        . .venv/bin/activate && streamlit run src/app.py

---

## 4️⃣ Criar arquivo `.env`

Na raiz do projeto:

    OPENAI_API_KEY=sua_chave_aqui

---

## 5️⃣ Executar setup completo

    make setup

---

## 6️⃣ Rodar aplicação

    make run

---

# 🧠 Como funciona

1. Carrega dados da fatura  
2. Carrega regras financeiras  
3. Monta contexto estruturado  
4. Envia para o modelo da OpenAI  
5. Retorna resposta ao usuário  

---

## 💬 Exemplos de Perguntas

- Qual o valor total da minha fatura?  
- Qual foi minha maior compra?  
- Tenho compras parceladas?  
- O que acontece se eu pagar só o mínimo?  

---

## 🔒 Boas Práticas

- Grounding com dados estruturados  
- Redução de alucinação  
- Separação de responsabilidades  
- Uso de ambiente virtual (.venv)  
- Uso de variáveis de ambiente (.env)  

---

## ⚠️ Aviso

Projeto com dados fictícios para fins educacionais.

---

## ⭐ Próximos Passos

- Memória de conversa  
- Análise automática com pandas  
- Upload de PDF  
- Deploy (Streamlit Cloud)  

---

## 🛠 Tecnologias

- Python  
- Streamlit  
- OpenAI API  
- python-dotenv  

---

<p align="center">
  Feito com 💻 + ☕
</p>