"""
Q3.2 — Consumo robusto de API paginada (5 pts)

Requisitos:
- Consome API REST paginada fictícia, persiste em .parquet, log estruturado em JSON.
- Retry com backoff exponencial em 429 e 5xx; respeitar header Retry-After.
- Circuit breaker simples (parar após N falhas consecutivas).
- Log com: total de páginas, total de registros, tempo total, erros por tipo, taxa de sucesso.
- Idempotência: reexecução não deve duplicar registros já persistidos.
"""

# TODO: implementar
