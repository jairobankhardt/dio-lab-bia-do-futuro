---

## Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot interativo desenvolvido em **Streamlit**, onde o usuário pode conversar com o agente e fazer perguntas sobre sua fatura |
| LLM | Modelo de linguagem (ex: **GPT via API**) responsável por interpretar perguntas em linguagem natural e gerar respostas explicativas |
| Base de Conhecimento | Dados da fatura armazenados em formato estruturado (**JSON ou CSV**) contendo informações como transações, valor total da fatura, pagamento mínimo e categorias de gasto |
| Validação | Camada de verificação que garante que as respostas utilizem apenas dados presentes na base da fatura e evita respostas inventadas pela IA |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] Agente responde apenas com base nos dados da fatura fornecida  
- [x] Respostas incluem referência aos dados utilizados (valores da fatura ou transações)  
- [x] Quando não possui informação suficiente, o agente informa explicitamente ao usuário  
- [x] O agente não realiza recomendações financeiras complexas ou personalizadas sem informações suficientes  

---

### Limitações Declaradas
> O que o agente NÃO faz?

O agente possui as seguintes limitações explícitas:

- não acessa contas bancárias reais ou dados financeiros externos  
- não executa pagamentos ou transações financeiras  
- não substitui aconselhamento financeiro profissional  
- não fornece recomendações de investimento personalizadas  
- depende exclusivamente das informações de fatura fornecidas para gerar respostas  
- não possui acesso a dados em tempo real do banco ou operadora do cartão  

Seu objetivo é **explicar e interpretar informações da fatura do cartão**, ajudando o usuário a compreender melhor seus gastos e possíveis impactos financeiros.