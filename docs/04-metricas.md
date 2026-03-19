# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do agente foi realizada de duas formas complementares:

1. **Testes estruturados:** Foram definidos cenários com perguntas específicas e respostas esperadas com base nos dados da fatura;
2. **Feedback qualitativo:** Testes informais foram realizados simulando diferentes tipos de perguntas de usuários para avaliar clareza, utilidade e segurança das respostas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu corretamente com base na fatura? | Perguntar "Qual o valor total da fatura?" e verificar se o valor está correto |
| **Segurança** | O agente evita inventar informações? | Perguntar algo fora da fatura e verificar se ele admite não saber |
| **Coerência** | A resposta é lógica e consistente com os dados? | Perguntar sobre maior gasto e verificar se corresponde à maior transação |
| **Clareza** | A resposta é compreensível para o usuário? | Perguntar sobre pagamento mínimo e avaliar se a explicação é simples |

> **Nota:** Os testes foram realizados considerando um cliente fictício representado pelos dados da fatura (`fatura_cartao.json`).

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de valor da fatura
- **Pergunta:** "Qual o valor total da minha fatura?"
- **Resposta esperada:** Valor total presente no JSON da fatura
- **Resultado:** [x] Correto  [ ] Incorreto

---

### Teste 2: Identificação da maior compra
- **Pergunta:** "Qual foi minha maior compra?"
- **Resposta esperada:** Maior valor entre as transações
- **Resultado:** [x] Correto  [ ] Incorreto

---

### Teste 3: Explicação de pagamento mínimo
- **Pergunta:** "O que acontece se eu pagar só o mínimo?"
- **Resposta esperada:** Explicação baseada nas regras do cartão (crédito rotativo e juros)
- **Resultado:** [x] Correto  [ ] Incorreto

---

### Teste 4: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo amanhã?"
- **Resposta esperada:** O agente informa que só trata de faturas e finanças
- **Resultado:** [x] Correto  [ ] Incorreto

---

### Teste 5: Informação inexistente
- **Pergunta:** "Qual foi meu gasto em viagens internacionais?"
- **Resposta esperada:** O agente informa que essa informação não está disponível
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

### O que funcionou bem:

- O agente respondeu corretamente perguntas diretas sobre a fatura (valor total, compras, categorias);
- As respostas foram claras, organizadas e com linguagem acessível;
- O agente evitou inventar informações quando os dados não estavam disponíveis;
- Boa integração entre dados estruturados (JSON) e respostas do modelo;
- A experiência do usuário foi simples e intuitiva.

---

### O que pode melhorar:

- O agente ainda depende da qualidade dos dados do JSON (não há validação robusta);
- Não há memória de conversa (cada pergunta é tratada isoladamente);
- Não há análise automática de gastos (ex: resumo por categoria);
- Interface ainda simples (poderia evoluir para formato de chat);
- Suporte a PDF ainda não implementado (planejado para evolução futura).

---

## Métricas Avançadas (Opcional)

Embora não tenham sido implementadas ferramentas de observabilidade completas, alguns aspectos foram considerados:

- **Latência:** As respostas são geradas rapidamente, com tempo médio de poucos segundos;
- **Consumo de tokens:** Controlado pelo uso de contexto estruturado (JSON);
- **Taxa de erro:** Baixa, ocorrendo principalmente quando há problemas no formato do JSON.

Como evolução futura, podem ser integradas ferramentas como:

- LangWatch  
- LangFuse  

para monitoramento de uso, desempenho e qualidade das respostas.

---