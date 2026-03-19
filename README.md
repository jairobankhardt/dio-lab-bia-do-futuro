# 💳 Clara — Assistente Inteligente de Fatura de Cartão

> Transformando faturas complexas em respostas simples usando IA generativa

---

## 🚀 Sobre o Projeto

A **Clara** é uma agente financeira inteligente que ajuda usuários a entender suas faturas de cartão de crédito de forma simples, clara e interativa.

Em vez de analisar manualmente a fatura, o usuário pode fazer perguntas em linguagem natural como:

- "Qual o valor total da minha fatura?"
- "Qual foi minha maior compra?"
- "O que acontece se eu pagar só o mínimo?"

A Clara interpreta os dados da fatura e responde de forma **educativa, confiável e baseada em dados reais**.

---

## 🎯 Problema

Muitas pessoas têm dificuldade em entender a fatura do cartão de crédito.

As informações estão disponíveis, mas:

- são pouco intuitivas  
- exigem interpretação manual  
- não explicam o impacto financeiro  

Isso pode levar a decisões ruins, como pagar apenas o mínimo sem entender as consequências.

---

## 💡 Solução

A Clara resolve esse problema através de:

- IA generativa (LLM)
- Dados estruturados (JSON)
- Interface conversacional (Streamlit)

O usuário pode:

✔ Fazer perguntas em linguagem natural  
✔ Enviar sua própria fatura em JSON  
✔ Obter respostas claras e contextualizadas  

---

## ⚙️ Como Funciona

Fluxo da aplicação:

1. O usuário envia uma fatura (ou usa a padrão)  
2. Os dados são estruturados em JSON  
3. O contexto é enviado ao modelo de linguagem  
4. A Clara responde com base nos dados da fatura  

---

## 🧠 Arquitetura

    Usuário → Streamlit → Agente → LLM → Resposta

- app.py → Interface  
- agente.py → Lógica e IA  
- config.py → Configuração  

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

    docs/
    ├── 01-documentacao-agente.md
    ├── 02-base-conhecimento.md
    ├── 03-prompts.md
    ├── 04-metricas.md
    └── 05-pitch.md

---

## ⚡ Como Executar

### 1. Criar ambiente virtual

    python3 -m venv .venv
    source .venv/bin/activate

---

### 2. Instalar dependências

    pip install -r src/requirements.txt

---

### 3. Configurar chave da OpenAI

Crie um arquivo `.env` na raiz:

    OPENAI_API_KEY=sua_chave_aqui

---

### 4. Executar aplicação

    streamlit run src/app.py

---

## 💬 Teste Rápido

Após rodar o app, experimente perguntar:

- Qual o valor total da minha fatura?  
- Qual foi minha maior compra?  
- Tenho compras parceladas?  
- O que acontece se eu pagar só o mínimo?  

---

## 🔒 Segurança e Confiabilidade

A Clara foi projetada para evitar alucinações:

- Usa apenas dados da fatura  
- Não inventa valores  
- Informa quando não sabe  
- Segue regras definidas no prompt  

---

## 🚀 Diferenciais

- Uso de IA com dados estruturados (grounding)  
- Respostas baseadas exclusivamente na fatura  
- Upload dinâmico de JSON  
- Arquitetura simples e modular  
- Foco em educação financeira  

---

## 📊 Métricas

O agente foi avaliado com base em:

- Assertividade  
- Segurança  
- Coerência  
- Clareza  

Detalhes em:

    docs/04-metricas.md

---

## 🎥 Pitch

Apresentação do projeto:

👉 [Assistir ao pitch](https://www.loom.com/share/7c92cd31769d45d4bbd95bc63fd429a8)

    https://www.loom.com/share/7c92cd31769d45d4bbd95bc63fd429a8
---

## 🚧 Melhorias Futuras

A seguir estão algumas evoluções planejadas para o projeto:

### 📄 Suporte a PDF
- Permitir upload de faturas em PDF  
- Extração automática de dados usando IA  
- Conversão para JSON estruturado  

---

### 📊 Análise Automática de Gastos
- Identificar automaticamente:
  - maior gasto do mês  
  - categoria com maior consumo  
  - padrão de comportamento financeiro  
- Gerar insights sem necessidade de pergunta  

---

### 💬 Histórico de Conversa
- Implementar chat com memória  
- Manter contexto entre perguntas  
- Melhorar a experiência do usuário  

---

### 🛡 Validação de Dados
- Validar estrutura do JSON da fatura  
- Evitar erros causados por dados inválidos  
- Garantir maior robustez da aplicação  

---

### 🎨 Melhorias de Interface
- Interface em formato de chat (estilo WhatsApp/ChatGPT)  
- Melhor organização visual das respostas  
- Destaque para informações importantes  

---

### 📈 Métricas e Monitoramento
- Monitorar tempo de resposta  
- Avaliar qualidade das respostas  
- Acompanhar uso da aplicação  

---

### 🔐 Segurança Avançada
- Melhor tratamento de dados sensíveis  
- Controle de acesso por usuário  
- Logs de uso da aplicação  

---

## 🛠 Tecnologias Utilizadas

- Python  
- Streamlit  
- OpenAI API  
- python-dotenv  

---

## ⚠️ Observação

Este projeto utiliza dados fictícios e tem finalidade educacional.

---

## 👨‍💻 Autor

Jairo Bankhardt

Projeto desenvolvido como parte do desafio DIO - Lab BIA do Futuro