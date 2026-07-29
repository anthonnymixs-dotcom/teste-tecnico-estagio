# Seção 5 · APIs REST, webhooks e segurança de integração

## Q5.1 — Polling versus webhook (2 pts)
**Prompt:**
Não tenho experiência formal em arquitetura de integrações. Explique, em até 6 linhas, a diferença entre polling e webhook e cite dois cenários em que polling ainda é a melhor opção, mesmo quando existe webhook. Gere uma resposta objetiva para um teste técnico.

**Resposta:**

No polling, a aplicação consulta periodicamente a API para verificar se houve alterações. Já no webhook, o próprio sistema envia uma notificação automaticamente quando ocorre um evento. O polling ainda pode ser a melhor escolha quando é necessário realizar uma reconciliação periódica para garantir que nenhum evento foi perdido ou quando os webhooks do fornecedor apresentam baixa confiabilidade ou indisponibilidade temporária.

## Q5.2 — Cuidados ao receber webhooks de pagamento (4 pts)

Não possuo experiência prática implementando o recebimento de webhooks de pagamento nem mecanismos como autenticação HMAC, idempotência baseada em event_id ou tratamento de eventos fora de ordem. Preferi não apresentar uma resposta gerada por IA que eu não conseguiria defender tecnicamente durante uma entrevista. Caso precisasse implementar esse fluxo, estudaria a documentação do provedor de pagamentos, os requisitos de segurança e desenvolveria a solução de forma incremental, validando cada etapa antes da implantação.

## Q5.3 — Validação HMAC-SHA256 (2 pts)

Não possuo experiência prática implementando validação de assinaturas HMAC-SHA256 para webhooks. Embora conheça o propósito desse mecanismo (garantir autenticidade e integridade das requisições), não me sinto confortável em escrever um trecho de código que não conseguiria explicar tecnicamente. Em um cenário real, estudaria a documentação do provedor da API, as bibliotecas recomendadas para Python e validaria a implementação com testes antes da utilização em produção. Preferi não apresentar uma solução gerada por IA que eu não conseguiria defender.

## Q5.4 — Versionamento de API (2 pts)

**Prompt:**
Não trabalhando diretamente com versionamento de APIs. Responda, em até 5 linhas, como proteger uma operação quando uma API externa sofre breaking changes frequentes.

**Resposta:**

Sempre que possível, utilizaria uma versão fixa da API em vez da versão mais recente. Antes de atualizar, validaria a integração em ambiente de testes e monitoraria alterações na documentação e nos changelogs do fornecedor. Além disso, manteria tratamento de erros e logs para identificar rapidamente falhas após mudanças e permitir uma reversão caso necessário.