# Seção 1 · Perfil profissional e contexto técnico

## Q1.1 — Automação em produção (3 pts)

*Descreva, em até 12 linhas: problema original e relevância; stack e decisões de arquitetura; ganho mensurável (tempo, custo, erro ou risco) com número; o que faria diferente hoje.*

Desenvolvi uma automação em Python para obter os relatórios XPerformance dos clientes da XP. A RPA existente utilizava Selenium com XPath para navegar pelo portal, mas apresentava falhas frequentes devido a alterações na interface e ao uso de Shadow DOM, exigindo manutenção recorrente. Durante a análise do fluxo, identifiquei que cada relatório possuía uma URL parametrizada pelo número da conta e pela data de referência. Redesenhei a solução para gerar essas URLs dinamicamente a partir de uma planilha Excel com mais de 200 contas e do mês informado pelo usuário, eliminando a dependência da navegação na interface. Embora a geração de cada relatório ainda leve cerca de um minuto no portal da XP, o processo passou a ser totalmente automatizado, permitindo que o operador execute outras atividades enquanto a rotina é concluída sem intervenção. A solução também praticamente eliminou a necessidade de manutenção mensal da automação. Utilizei Python e Excel. Hoje adicionaria uma interface mais amigável para qualquer um que não tenha conhecimento de py conseguir rodar.


## Q1.2 — Stack declarada (2 pts)

*Classifique cada ferramenta em: uso esporádico, uso regular ou uso avançado.*

| Ferramenta / Tecnologia | Nível | Experiência |
|---|---|---|
| Python | *Avançado* | Desenvolvimento de RPAs e automações em produção, manipulação de dados, integração entre sistemas e processamento de arquivos. |
| Selenium | *Avançado* | Desenvolvimento e manutenção de automações web, web scraping e interação com aplicações web. Experiência em otimização de fluxos utilizando XPath, manipulação de Shadow DOM e automação de portais corporativos. |
| pandas | *Avançado* | Manipulação, limpeza e transformação de bases de dados, principalmente em Excel. Conversão de planilhas para JSON e estruturação de dados para automações. |
| SQL | *Esporádico* | Tenho experiência apenas com consultas básicas. Nas questões de SQL avançado (CTEs e Window Functions), utilizei ChatGPT como apoio para construir a sintaxe e compreender a solução, revisando a lógica antes da entrega. |
| Deluge (Zoho CRM) | *Regular* | Desenvolvimento de automações, workflows e regras de negócio no Zoho CRM para automatizar processos internos e integrações entre módulos. |
| Microsoft Excel | *Avançado* | Manipulação de grandes bases de dados, conferência de informações e integração com automações desenvolvidas em Python. |
| APIs REST | *Regular* | Consumo de APIs e integração de dados em automações e processos operacionais.|
| Comdinheiro | *Avançado* | Experiência diária com o consolidador de carteiras, incluindo análise de posições, conferência patrimonial, integração de dados via APIs e boletagem de ativos. |
| Zoho CRM | *Regular* | Configuração de processos, automações, workflows e customizações utilizando Deluge. |
| Pipedrive |*Esporádico* | Utilização para acompanhamento de pipeline comercial e gestão de oportunidades. |
| Power BI | *Esporádico* | Utilização acadêmica para construção de dashboards e visualização de dados. |
| Ferramentas de IA (ChatGPT e Claude) | *Regular* | Apoio ao desenvolvimento de código, debugging, documentação e aceleração do desenvolvimento de automações. |