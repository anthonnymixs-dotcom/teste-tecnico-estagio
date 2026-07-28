# Seção 2 · SQL avançado aplicado a dados operacionais

## Q2.0 — Modelo de dados (referência, 0 pts)

```
clientes (id_cliente, nome, cpf, data_cadastro, status_kyc, segmento)
aportes (id_aporte, id_cliente, valor, data_aporte, meio_pagamento, status)
investimentos (id_investimento, id_cliente, id_produto, valor_investido, data_investimento)
produtos (id_produto, nome_produto, classe, taxa_a_a, data_vencimento)
liquidacoes (id_liquidacao, id_investimento, valor_pago, data_pagamento, tipo)
```

---

## Q2.1 — Volume por meio de pagamento (2 pts)

*Volume total de aportes liquidados no mês corrente, agrupado por meio de pagamento, com % de participação, ordenado do maior para o menor.*

```sql
-- sua query aqui
```

**Premissas assumidas:**
- [ex: "mês corrente" = mês atual do sistema, considerando apenas status = 'LIQUIDADO']

---

## Q2.2 — Aportistas sem investimento (3 pts)

*Clientes que fizeram aporte sem investimento subsequente em até 7 dias, nos últimos 30 dias. Use CTE.*

```sql
-- sua query aqui
```

---

## Q2.3 — Cohort de retenção (4 pts)

*Cohort por mês de primeiro aporte, com % de clientes com 2º aporte em 30/60/90 dias.*

```sql
-- sua query aqui
```

---

## Q2.4 — Análise de queda atípica (3 pts)

*Em até 8 linhas: como investigar uma queda atípica no volume diário de aportes usando apenas SQL e Metabase, sem acionar Engenharia. Inclua hipóteses ordenadas, mínimo 4 dimensões de quebra, critério objetivo para diferenciar ruído de incidente, ponto de escalonamento.*

[Sua resposta aqui]
