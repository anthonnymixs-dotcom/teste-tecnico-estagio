# Seção 9 · Gestão de incidentes N2 e análise de causa raiz

## Q9.1 — Sequência de ações nas próximas 2 horas (4 pts)
A primeira coisa que faria seria confirmar se os três casos realmente têm relação entre si, verificando o horário dos PIX, os comprovantes apresentados pelos clientes, o status das transações e se existe algum padrão entre elas. Como os três relatos aconteceram na segunda-feira e os aportes foram feitos no domingo, investigaria se houve alguma falha na conciliação ou no processamento dos pagamentos. No meu estágio em operações de câmbio, já passei por situações semelhantes de liquidações pendentes e aprendi que o primeiro passo é sempre validar as informações antes de assumir a causa do problema.

Se identificar que os casos podem estar relacionados, acionaria primeiro a equipe de Pagamentos para verificar se houve alguma falha no processamento das transações. Caso exista indício de erro no sistema ou na integração, envolveria a equipe de Engenharia. Se o impacto atingir um número maior de clientes ou houver risco de descumprimento de SLA, comunicaria também a liderança para que acompanhe o incidente.

Durante toda a investigação, manteria os clientes informados com transparência. Assim como fazia no estágio, explicaria que a situação está sendo analisada pelas equipes responsáveis, que estamos acompanhando o caso de perto e que retornaremos assim que tivermos uma atualização. Evitaria informar uma causa ou um prazo antes da confirmação da investigação.

Consideraria o incidente como sistêmico caso outros clientes apresentassem o mesmo problema ou fosse identificada uma falha comum no processamento. Caso contrário, trataria os casos como ocorrências isoladas. Ao final, documentaria a causa identificada, o impacto, as ações realizadas, as equipes envolvidas e as medidas adotadas para evitar que o problema volte a acontecer.

## Q9.2 — Análise de causa raiz (5 Whys) (2 pts)
1. Por que os aportes PIX não apareceram para os clientes?
Porque o job de conciliação de domingo falhou e os aportes não foram processados corretamente.

2. Por que o job de conciliação falhou?
Porque ocorreu um erro durante a execução do processo.

3. Por que esse erro não foi identificado imediatamente?
Porque a falha ocorreu de forma silenciosa, sem gerar alertas, breaks ou notificações para a equipe.

4. Por que não existiam alertas para esse tipo de falha?
Porque o processo não possuía monitoramento adequado para validar a conclusão da conciliação.

5. Por que o monitoramento não existia?
Porque o processo foi implementado sem controles suficientes para detectar falhas automaticamente.

**Causa raiz:**
Ausência de monitoramento e alertas para identificar falhas no processo de conciliação.

**Ação corretiva:**
Executar novamente a conciliação dos aportes afetados, validar os valores e creditar corretamente os clientes impactados.

**Ação preventiva:**
Implementar monitoramento automático do job, com alertas em caso de falha ou ausência de execução, além de um processo de validação que confirme que todas as transações esperadas foram conciliadas.

## Q9.3 — Post mortem blameless (2 pts)

Não possuo experiência prática conduzindo post mortems formais. Utilizei IA para compreender a metodologia e estruturar a resposta abaixo. Revisei o conteúdo antes do envio.

**Prompt:**
Explique, em no máximo oito linhas, o que é um post mortem blameless. Liste cinco elementos que ele deve conter e um critério para decidir quando um incidente merece um post mortem formal. 

**Resposta:**
Um post mortem blameless é uma análise realizada após um incidente com o objetivo de entender o que aconteceu e evitar que o problema se repita, sem buscar culpados. Ele deve conter: descrição do incidente, linha do tempo dos acontecimentos, causa raiz, impacto gerado e plano de ações para prevenção. Na minha visão, um post mortem formal deve ser realizado quando o incidente gera impacto relevante para clientes, descumprimento de SLA, perdas financeiras ou risco de recorrência.
