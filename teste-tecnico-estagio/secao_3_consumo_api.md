# Seção 3 · Consumo de API

## Q3.2 — Consumo robusto de API paginada (5 pts)

**Resposta:**

Não possuo experiência prática implementando uma solução com todos os requisitos solicitados (retry com backoff exponencial, circuit breaker, persistência em Parquet e idempotência). Em um cenário real, minha abordagem seria estudar a documentação das bibliotecas recomendadas (requests/httpx, pandas/pyarrow e logging), implementar a solução incrementalmente, validar cada requisito com testes e realizar revisões técnicas antes da implantação em produção. Optei por não entregar um código gerado por IA que eu não conseguiria explicar ou manter.

## Q3.3 — Code review: função em produção (~200 mil itens/dia) (5 pts)

Função original:

def aplicar_taxa(lista):
    resultado = []
    for item in lista:
        if item['classe'] == 'DEB':
            resultado.append(item['valor'] * 1.12)
        elif item['classe'] == 'CRI':
            resultado.append(item['valor'] * 1.10)
        elif item['classe'] == 'CRA':
            resultado.append(item['valor'] * 1.09)
        else:
            resultado.append(item['valor'])
    return resultado

Tarefa: identificar no mínimo 4 fragilidades, reescrever versão mais robusta
e escalável, explicando cada decisão (manutenibilidade, performance,
edge cases, testabilidade).

**Resposta:**

Fragilidade 1 - Tratamento de classes inválidas ou ausentes.

Caso um item venha sem uma classe válida, o código simplesmente retorna o valor original sem indicar que houve uma inconsistência. Isso pode mascarar problemas na origem dos dados e dificultar a identificação de erros operacionais.

Fragilidade 2 – Taxas fixas na lógica da função

As taxas estão definidas diretamente nos blocos if/elif, o que dificulta a manutenção do código. Uma alternativa seria centralizar essas informações em um dicionário, por exemplo:

```
TAXAS = {
    "DEB": 1.12,
    "CRI": 1.10,
    "CRA": 1.09
}
```

Dessa forma, a função precisaria apenas buscar a taxa correspondente (taxa = TAXAS.get(classe)), e a inclusão de uma nova classe ou alteração de uma taxa exigiria apenas modificar o dicionário, sem alterar a lógica do processamento.

Fragilidade 3 - Ausência de logs.

A função não registra o processamento realizado nem possíveis inconsistências. Em produção, logs ajudam a monitorar a execução, identificar registros inválidos e facilitar a investigação de falhas.

Fragilidade 4 - Falta de validação do valor de entrada.

Imagine que chegue um registro assim:

```
{
    "classe": "DEB",
    "valor": None
}
```

A multiplicação pode falhar ou produzir um resultado inesperado, dependendo do tipo do dado. Para um processamento de aproximadamente 200 mil itens por dia, é importante validar os dados antes de aplicar a taxa e decidir como tratar registros inválidos (descartar, registrar em log ou encaminhar para uma fila de erros).
