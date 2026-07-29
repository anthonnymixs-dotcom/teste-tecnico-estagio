# Seção 2 · SQL avançado aplicado a dados operacionais

## Q2.0 — Modelo de dados (referência, 0 pts)


**Premissa:** não possuo experiência prática desenvolvendo consultas SQL além de consultas simples. Para resolver a questão, utilizei IA como apoio.

Base utilizada nas questões Q2.1 a Q2.4
```sql
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(14),
    data_cadastro DATE,
    status_kyc VARCHAR(20),
    segmento VARCHAR(30)
);

CREATE TABLE aportes (
    id_aporte INT PRIMARY KEY,
    id_cliente INT,
    valor DECIMAL(12,2),
    data_aporte DATE,
    meio_pagamento VARCHAR(20),
    status VARCHAR(20)
);

CREATE TABLE investimentos (
    id_investimento INT PRIMARY KEY,
    id_cliente INT,
    id_produto INT,
    valor_investido DECIMAL(12,2),
    data_investimento DATE
);

CREATE TABLE produtos (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(50),
    classe VARCHAR(30),
    taxa_a_a DECIMAL(5,2),
    data_vencimento DATE
);

CREATE TABLE liquidacoes (
    id_liquidacao INT PRIMARY KEY,
    id_investimento INT,
    valor_pago DECIMAL(12,2),
    data_pagamento DATE,
    tipo VARCHAR(30)
);

INSERT INTO clientes VALUES
(1,'Ana','111','2024-01-10','APROVADO','Varejo'),
(2,'Bruno','222','2024-02-15','APROVADO','Private'),
(3,'Carlos','333','2024-03-12','APROVADO','Varejo'),
(4,'Daniela','444','2024-04-01','APROVADO','Private');

INSERT INTO aportes VALUES
(1,1,10000,CURRENT_DATE-5,'PIX','LIQUIDADO'),
(2,2,5000,CURRENT_DATE-10,'TED','LIQUIDADO'),
(3,3,8000,CURRENT_DATE-15,'PIX','LIQUIDADO'),
(4,4,12000,CURRENT_DATE-20,'BOLETO','LIQUIDADO'),
(5,1,4000,CURRENT_DATE-40,'PIX','LIQUIDADO');

INSERT INTO produtos VALUES
(1,'CDB','Renda Fixa',12,'2027-01-01'),
(2,'Fundo','Multimercado',0,'2030-01-01');

INSERT INTO investimentos VALUES
(1,1,1,10000,CURRENT_DATE-2),
(2,2,2,5000,CURRENT_DATE-1);

INSERT INTO liquidacoes VALUES
(1,1,10500,CURRENT_DATE,'Resgate');
```

---

## Q2.1 — Volume por meio de pagamento (2 pts)

*Volume total de aportes liquidados no mês corrente, agrupado por meio de pagamento, com % de participação, ordenado do maior para o menor.*

**Prompt utilizado:**

"Considere o seguinte schema:

clientes (id_cliente, nome, cpf, data_cadastro, status_kyc, segmento)
aportes (id_aporte, id_cliente, valor, data_aporte, meio_pagamento, status)

Escreva uma consulta SQL que:

considere apenas aportes com status = 'LIQUIDADO';
filtre apenas o mês corrente;
agrupe por meio de pagamento;
some o volume financeiro;
calcule o percentual que cada meio representa do total do mês;
ordene do maior para o menor volume.

Explique brevemente a lógica da consulta."

```sql
SELECT
    meio_pagamento,
    SUM(valor) AS volume_total,
    ROUND(
        100.0 * SUM(valor) / SUM(SUM(valor)) OVER (),
        2
    ) AS percentual_participacao
FROM aportes
WHERE status = 'LIQUIDADO'
  AND DATE_TRUNC('month', data_aporte) = DATE_TRUNC('month', CURRENT_DATE)
GROUP BY meio_pagamento
ORDER BY volume_total DESC;
```
---

## Q2.2 — Aportistas sem investimento (3 pts)

*Clientes que fizeram aporte sem investimento subsequente em até 7 dias, nos últimos 30 dias. Use CTE.*

**Prompt utilizado:**

Considere o seguinte schema:

clientes (id_cliente, nome, cpf, data_cadastro, status_kyc, segmento)
aportes (id_aporte, id_cliente, valor, data_aporte, meio_pagamento, status)
investimentos (id_investimento, id_cliente, id_produto, valor_investido, data_investimento)

Escreva uma consulta SQL utilizando CTE que retorne os clientes que realizaram um aporte nos últimos 30 dias e que não realizaram nenhum investimento em até 7 dias após esse aporte.

Retorne:

id_cliente
nome
data_aporte
valor_aporte
dias_decorridos_desde_aporte

Explique brevemente a lógica utilizada.

```sql
WITH aportes_recentes AS (
    SELECT
        a.id_cliente,
        c.nome,
        a.data_aporte,
        a.valor,
        CURRENT_DATE - a.data_aporte AS dias_decorridos_desde_aporte
    FROM aportes a
    JOIN clientes c
        ON c.id_cliente = a.id_cliente
    WHERE a.data_aporte >= CURRENT_DATE - INTERVAL '30 days'
)

SELECT
    ar.id_cliente,
    ar.nome,
    ar.data_aporte,
    ar.valor AS valor_aporte,
    ar.dias_decorridos_desde_aporte
FROM aportes_recentes ar
WHERE NOT EXISTS (
    SELECT 1
    FROM investimentos i
    WHERE i.id_cliente = ar.id_cliente
      AND i.data_investimento BETWEEN ar.data_aporte
                                  AND ar.data_aporte + INTERVAL '7 days'
)
ORDER BY ar.data_aporte DESC;
```

---

## Q2.3 — Cohort de retenção (4 pts)

*Cohort por mês de primeiro aporte, com % de clientes com 2º aporte em 30/60/90 dias.*

**Prompt utilizado:**

"Considere o seguinte schema:

clientes
aportes

Escreva uma consulta SQL utilizando CTEs e/ou Window Functions que faça uma análise de cohort por mês do primeiro aporte de cada cliente.

Para cada cohort (YYYY-MM), calcule:

total_clientes
percentual de clientes que fizeram o segundo aporte em até 30 dias
percentual em até 60 dias
percentual em até 90 dias

Explique passo a passo a lógica da consulta."

```sql
WITH primeiro_aporte AS (
    SELECT
        id_cliente,
        MIN(data_aporte) AS primeiro_aporte
    FROM aportes
    GROUP BY id_cliente
),

segundo_aporte AS (
    SELECT
        p.id_cliente,
        p.primeiro_aporte,
        MIN(a.data_aporte) AS segundo_aporte
    FROM primeiro_aporte p
    LEFT JOIN aportes a
        ON a.id_cliente = p.id_cliente
       AND a.data_aporte > p.primeiro_aporte
    GROUP BY p.id_cliente, p.primeiro_aporte
)

SELECT
    TO_CHAR(primeiro_aporte, 'YYYY-MM') AS cohort,
    COUNT(*) AS total_clientes,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN segundo_aporte <= primeiro_aporte + INTERVAL '30 days'
                THEN 1 ELSE 0
            END
        ) / COUNT(*), 2
    ) AS pct_retorno_30d,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN segundo_aporte <= primeiro_aporte + INTERVAL '60 days'
                THEN 1 ELSE 0
            END
        ) / COUNT(*), 2
    ) AS pct_retorno_60d,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN segundo_aporte <= primeiro_aporte + INTERVAL '90 days'
                THEN 1 ELSE 0
            END
        ) / COUNT(*), 2
    ) AS pct_retorno_90d

FROM segundo_aporte
GROUP BY TO_CHAR(primeiro_aporte, 'YYYY-MM')
ORDER BY cohort;
```

---

## Q2.4 — Análise de queda atípica (3 pts)

*Em até 8 linhas: como investigar uma queda atípica no volume diário de aportes usando apenas SQL e Metabase, sem acionar Engenharia. Inclua hipóteses ordenadas, mínimo 4 dimensões de quebra, critério objetivo para diferenciar ruído de incidente, ponto de escalonamento.*

**Prompt utilizado:**

"Tenho pouca experiência com SQL avançado e preciso responder uma questão dissertativa para um teste técnico.

Pergunta:

"Em até 8 linhas: como investigar uma queda atípica no volume diário de aportes usando apenas SQL e Metabase, sem acionar Engenharia.
Inclua:

hipóteses ordenadas;
no mínimo 4 dimensões de quebra;
critério objetivo para diferenciar ruído de incidente;
ponto de escalonamento ao time técnico."

Gere uma resposta objetiva (máximo 8 linhas), com foco em operações financeiras e investigação de incidentes, sem escrever consultas SQL."

**Resposta:**
Inicialmente verificaria se a queda é generalizada ou concentrada em um grupo específico. Em seguida, analisaria o volume de aportes segmentando por meio de pagamento, segmento de clientes, canal de origem e status da operação, comparando com dias equivalentes das últimas semanas para identificar sazonalidade. Também avaliaria se houve aumento de aportes pendentes, recusados ou cancelados. Consideraria um incidente quando a queda ultrapassasse a variação histórica esperada ou persistisse por mais de um período de análise. Caso a investigação indique falha sistêmica, indisponibilidade de integrações ou inconsistências nos dados, escalaria o caso para a Engenharia apresentando as evidências levantadas.