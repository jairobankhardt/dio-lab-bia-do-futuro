# Base de Conhecimento

## Dados Utilizados

A base de conhecimento do agente é composta por dois arquivos estruturados que representam uma fatura fictícia de cartão de crédito e as regras financeiras relacionadas ao funcionamento do cartão.

| Arquivo | Formato | Utilização no Agente |
|--------|--------|----------------------|
| `fatura_cartao.json` | JSON | Contém os dados da fatura e todas as transações do período. Utilizado para interpretar gastos, identificar categorias, encontrar maiores compras e responder perguntas sobre a fatura |
| `regras_cartao.json` | JSON | Contém regras e explicações sobre conceitos financeiros do cartão de crédito, como pagamento mínimo, crédito rotativo e parcelamento da fatura |

Esses dados permitem que o agente interprete a fatura e responda perguntas como:

- Qual o valor total da minha fatura?
- Qual é o pagamento mínimo?
- Em qual categoria gastei mais?
- Qual foi minha maior compra?
- Tenho compras parceladas?
- O que acontece se eu pagar apenas o mínimo?

---

# Adaptações nos Dados

Os arquivos mockados originalmente fornecidos no desafio incluíam dados voltados para outros tipos de agentes financeiros, como recomendação de investimentos e histórico de atendimento.

Para adequar a base de conhecimento ao objetivo deste projeto (interpretação de fatura de cartão de crédito), foi criada uma nova estrutura de dados composta por:

- `fatura_cartao.json`, contendo:
  - dados do cliente
  - resumo da fatura
  - lista completa de transações do período

- `regras_cartao.json`, contendo:
  - regras financeiras do cartão
  - explicações sobre conceitos como pagamento mínimo, crédito rotativo e parcelamento

Essa estrutura se aproxima mais de uma **fatura real de cartão de crédito**, que normalmente apresenta o resumo da fatura junto com a lista de compras realizadas no período.

Todos os dados utilizados são **fictícios e destinados apenas ao contexto educacional do desafio**.

---

# Estratégia de Integração

## Como os dados são carregados?

Os arquivos JSON são carregados no início da execução da aplicação utilizando Python.

Exemplo de carregamento:

```python
import json

with open("data/fatura_cartao.json") as f:
    fatura = json.load(f)

with open("data/regras_cartao.json") as f:
    regras = json.load(f)
```

### Como os dados são usados no prompt?

Os dados da base de conhecimento são inseridos no contexto enviado ao modelo de linguagem para que o agente consiga interpretar corretamente a fatura e explicar conceitos financeiros ao usuário.

A estratégia adotada consiste em incluir dois blocos principais no contexto do prompt:

1. **Regras do cartão de crédito** – utilizadas para explicar conceitos financeiros.
2. **Dados da fatura do cliente** – utilizados para responder perguntas específicas sobre gastos.

Esses dados são inseridos no contexto do agente antes da pergunta do usuário.

```txt
REGRAS DO CARTÃO (JSON):
{
  "taxas": {
    "pagamento_minimo_percentual": 15,
    "juros_rotativo_mensal_percentual": 12,
    "multa_atraso_percentual": 2,
    "juros_atraso_mensal_percentual": 1,
    "parcelamento_fatura_juros_percentual": 8
  },

  "explicacoes": {
    "pagamento_minimo": "O pagamento mínimo é o valor mínimo que precisa ser pago para evitar atraso na fatura. Quando o cliente paga apenas o mínimo, o restante da fatura entra no crédito rotativo e passa a gerar juros.",

    "credito_rotativo": "O crédito rotativo ocorre quando o cliente paga menos que o valor total da fatura. O valor restante passa a gerar juros mensais até que seja quitado.",

    "parcelamento_fatura": "O parcelamento da fatura permite dividir o valor total em parcelas mensais. Cada parcela possui juros, normalmente menores que os do crédito rotativo.",

    "limite_cartao": "O limite do cartão representa o valor máximo que pode ser utilizado em compras. Conforme a fatura é paga, o limite é liberado novamente.",

    "pagamento_total": "O pagamento total da fatura evita a cobrança de juros e mantém o uso do cartão sem encargos financeiros."
  }
}

DADOS DA FATURA (JSON):
{
  "cliente": {
    "nome": "João Silva",
    "cartao": "Visa Platinum"
  },

  "fatura": {
    "mes_referencia": "2026-02",
    "vencimento": "2026-02-20",
    "valor_total": 3222.15,
    "pagamento_minimo": 483.32,
    "limite_total": 5000,
    "limite_disponivel": 1777.85
  },

  "transacoes": [
    {
      "data": "2026-02-01",
      "estabelecimento": "Amazon",
      "categoria": "Compras Online",
      "descricao": "Fone de ouvido Bluetooth",
      "valor": 289.90,
      "parcelamento": "1/1"
    },
    {
      "data": "2026-02-02",
      "estabelecimento": "Supermercado Condor",
      "categoria": "Alimentação",
      "descricao": "Compras do mês",
      "valor": 356.45,
      "parcelamento": "1/1"
    },
    {
      "data": "2026-02-07",
      "estabelecimento": "Magazine Luiza",
      "categoria": "Compras Online",
      "descricao": "Smart TV 50\"",
      "valor": 329.90,
      "parcelamento": "3/10"
    },
    {
      "data": "2026-02-12",
      "estabelecimento": "Restaurante Madalosso",
      "categoria": "Alimentação",
      "descricao": "Jantar família",
      "valor": 186.00,
      "parcelamento": "1/1"
    },
    {
      "data": "2026-02-21",
      "estabelecimento": "Amazon",
      "categoria": "Compras Online",
      "descricao": "Teclado mecânico",
      "valor": 459.90,
      "parcelamento": "2/6"
    }
  ]
}

```

## Exemplo de Contexto Montado

Abaixo está um exemplo simplificado de como os dados da base de conhecimento podem ser organizados antes de serem enviados ao agente. O objetivo é fornecer ao modelo de linguagem informações suficientes sobre as regras do cartão e os dados da fatura para que ele consiga responder corretamente às perguntas do usuário.

Contexto enviado ao agente:

(regras)

Pagamento mínimo: 15% do valor total da fatura  
Juros do crédito rotativo: 12% ao mês  
Multa por atraso: 2%

Explicações:
- Pagamento mínimo: valor mínimo que deve ser pago para evitar atraso na fatura.
- Crédito rotativo: ocorre quando o cliente paga menos que o valor total da fatura e o saldo restante passa a gerar juros.
- Parcelamento da fatura: opção de dividir o valor total em parcelas mensais com incidência de juros.

(fatura)

Cliente: João Silva  
Cartão: Visa Platinum  

Mês da fatura: Fevereiro de 2026  
Vencimento: 20/02/2026  

Valor total da fatura: R$ 3.222,15  
Pagamento mínimo: R$ 483,32  

Transações:
- 01/02: Amazon — R$ 289,90
- 02/02: Supermercado Condor — R$ 356,45
- 07/02: Magazine Luiza — R$ 329,90 (3/10)
- 12/02: Restaurante Madalosso — R$ 186,00
- 21/02: Amazon — R$ 459,90 (2/6)

Pergunta do usuário:

Qual foi minha maior compra nesta fatura?

Com esse contexto, o agente consegue analisar as transações da fatura e identificar corretamente que a maior compra foi **Amazon — R$ 459,90**, além de poder explicar conceitos relacionados ao funcionamento do cartão caso o usuário faça perguntas adicionais.