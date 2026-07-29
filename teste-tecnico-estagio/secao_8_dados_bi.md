# Seção 8 · Análise de dados, BI e cultura analítica

## Q8.1 — Dashboard semanal de saúde operacional (4 pts)

Não possuo experiência direta na criação de dashboards operacionais para processos de pagamentos. Utilizei IA como apoio para estruturar uma proposta de indicadores e alertas, revisando o conteúdo antes do envio.

**Prompt:**
Considere um processo de pagamentos em uma fintech. Proponha um dashboard semanal de saúde operacional contendo entre 6 e 8 indicadores. Para cada indicador, informe nome, fórmula resumida, justificativa de uso e frequência de medição (diária, semanal ou mensal). Em seguida, proponha três alertas automáticos contendo a regra de disparo e o canal de notificação. Escreva em português simples, como resposta para um processo seletivo de tecnologia.


| Indicador                            | Fórmula resumida                                | Por que acompanhar?                | Frequência |
| ------------------------------------ | ----------------------------------------------- | ---------------------------------- | ---------- |
| Volume de pagamentos                 | Total de pagamentos processados                 | Mede a carga operacional da semana | Diário     |
| Taxa de sucesso                      | Pagamentos concluídos / Total de pagamentos     | Avalia a estabilidade do processo  | Diário     |
| Tempo médio de processamento         | Soma dos tempos / Total de pagamentos           | Identifica lentidão no fluxo       | Diário     |
| Taxa de falhas                       | Pagamentos com erro / Total de pagamentos       | Monitora problemas operacionais    | Diário     |
| Retrabalho                           | Pagamentos reprocessados / Total de pagamentos  | Mede eficiência do processo        | Semanal    |
| Cumprimento do SLA                   | Pagamentos dentro do SLA / Total                | Verifica atendimento aos prazos    | Diário     |
| Backlog                              | Pagamentos pendentes                            | Acompanha acúmulo de demanda       | Diário     |
| Tempo médio para resolução de falhas | Soma dos tempos de resolução / Número de falhas | Mede a velocidade de recuperação   | Semanal    |


**Alertas automáticos**

1. Queda na taxa de sucesso

Regra: taxa de sucesso inferior a 98%.
Canal: Slack para a equipe de Operações.

2. Crescimento do backlog

Regra: quantidade de pagamentos pendentes acima de 20% da média da última semana.
Canal: e-mail para o gestor da operação.

3. Aumento da taxa de falhas

Regra: taxa de falhas superior a 2% em um único dia.
Canal: Slack com alerta para Operações e Tecnologia.

## Q8.2 — Outliers e ruído estatístico (2 pts)

Não possuo experiência prática com análise estatística de séries temporais utilizando métodos como z-score ou IQR. Utilizei IA para compreender esses conceitos e estruturar uma resposta objetiva. Revisei o conteúdo antes do envio.

**Prompt:**
Explique, em no máximo seis linhas, como identificar e comunicar um outlier em uma série diária de aportes. Cite pelo menos dois métodos entre z-score, IQR, média móvel e decomposição sazonal. Explique também como diferenciar um ruído estatístico de um evento que exige investigação imediata. 

**Resposta:**
Para identificar um outlier, eu utilizaria métodos como z-score e IQR para verificar se um valor está muito acima ou abaixo do comportamento esperado. Depois compararia o resultado com o histórico recente e verificaria se existe alguma explicação conhecida, como uma campanha ou sazonalidade. Se houver uma justificativa, trataria como um ruído esperado. Caso o desvio não tenha uma causa aparente ou represente um impacto relevante no negócio, comunicaria a ocorrência à equipe responsável e iniciaria uma investigação para identificar a origem do problema.

## Q8.3 — Conflito com stakeholder de negócio (2 pts)

Eu explicaria que não é adequado alterar o relatório de forma que distorça os indicadores, pois isso compromete a confiabilidade das informações. Procuraria entender qual é a necessidade do Marketing e, se fizer sentido, criaria uma visão alternativa com filtros claramente identificados, mantendo também a versão oficial do relatório. Documentaria os critérios utilizados e registraria a solicitação para garantir transparência e facilitar consultas futuras.
