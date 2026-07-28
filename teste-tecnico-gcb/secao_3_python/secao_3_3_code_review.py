"""
Q3.3 — Code review: função em produção (~200 mil itens/dia) (5 pts)

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
"""

# --- Fragilidades identificadas ---
# 1. [ex: chaves mágicas 'DEB'/'CRI'/'CRA' e taxas hardcoded — difícil manter/auditar]
# 2. [...]
# 3. [...]
# 4. [...]

# --- Versão reescrita ---
# TODO: implementar

# --- Testes ---
# TODO: implementar (ex: pytest com casos por classe + edge cases)
