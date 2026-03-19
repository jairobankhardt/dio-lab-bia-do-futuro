# 🧠 Código da Aplicação

Este diretório contém a implementação do agente financeiro **Clara**, responsável por interpretar faturas de cartão de crédito utilizando IA generativa.

Aqui está toda a lógica da aplicação, incluindo:

- Interface (Streamlit)
- Integração com o modelo de IA
- Montagem de contexto estruturado
- Interpretação da fatura com base em dados

---

## 📁 Estrutura

    src/
    ├── app.py        # Interface do usuário (Streamlit)
    ├── agente.py     # Lógica do agente + integração com LLM
    ├── config.py     # Configurações (API Key, modelo)
    └── requirements.txt

---

## ⚙️ Componentes

### 🖥 app.py
Responsável pela interface da aplicação.

Funções principais:
- Upload de fatura em JSON
- Exibição dos dados da fatura
- Captura de perguntas do usuário
- Exibição das respostas do agente

---

### 🤖 agente.py
Responsável pela lógica do agente.

Funções principais:
- Carregar regras do cartão
- Montar contexto estruturado (fatura + regras)
- Enviar contexto para o modelo de linguagem
- Gerar respostas baseadas nos dados fornecidos

---

### ⚙️ config.py
Gerencia configurações da aplicação:

- Leitura da variável `OPENAI_API_KEY`
- Definição do modelo utilizado (`gpt-4o-mini`)

---

## 🔄 Fluxo da Aplicação

    Usuário → app.py → agente.py → OpenAI API → Resposta → app.py

---

## 📄 Formato da Fatura (JSON)

A aplicação espera um JSON com a seguinte estrutura:

    {
      "cliente": { "nome": "", "cartao": "" },
      "fatura": {
        "valor_total": 0,
        "pagamento_minimo": 0
      },
      "transacoes": [
        {
          "data": "",
          "estabelecimento": "",
          "valor": 0
        }
      ]
    }

Esse formato garante que o agente consiga interpretar corretamente os dados.

---

## 💬 Exemplo de Uso

Pergunta:

    Qual foi minha maior compra?

Resposta esperada:

    A maior compra registrada foi de R$ 459,90.

    Essa compra foi realizada na Amazon e está atualmente na parcela 2 de 6.

---

## 🤖 Modelo Utilizado

A aplicação utiliza o modelo:

    gpt-4o-mini

via API da OpenAI.

---

## ⚙️ Setup Completo

### 1️⃣ Criar `.gitignore`

Crie um arquivo `.gitignore` na raiz:

    .venv/
    __pycache__/
    *.pyc
    .env
    .streamlit/
    .vscode/

---

### 2️⃣ Configurar VSCode

Crie o arquivo:

    .vscode/settings.json

Conteúdo:

    {
      "python.defaultInterpreterPath": ".venv/bin/python"
    }

Isso faz o VSCode usar automaticamente o ambiente virtual.

---

### 3️⃣ Criar Makefile (automação)

Crie um arquivo `Makefile` na raiz:

    setup:
        python3 -m venv .venv
        . .venv/bin/activate && pip install -r src/requirements.txt

    run:
        . .venv/bin/activate && streamlit run src/app.py

---

### 4️⃣ Criar arquivo `.env`

Na raiz do projeto:

    OPENAI_API_KEY=sua_chave_aqui

---

### 5️⃣ Executar setup completo

    make setup

---

### 6️⃣ Rodar aplicação

    make run

---

## 🔒 Boas Práticas Aplicadas

- Separação de responsabilidades
- Uso de variáveis de ambiente (.env)
- Grounding com dados estruturados
- Controle de alucinação via prompt
- Uso de contexto explícito para respostas confiáveis

---

## 📌 Observação

Este diretório contém apenas a implementação técnica da aplicação.

Para visão geral do projeto, consulte:

    ../README.md