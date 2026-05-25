# 📓 Notebooks — Encontro 01 (Grupo de Estudo Fase 01)

> **Recorte do Tech Challenge:** Etapa 1 — Entendimento do Problema e Pipeline de Dados (Telco Churn).
>
> **Origem canônica:** [Disciplina 01 — Introdução ao Ciclo de Vida de Modelos, Aula 01](../../../../disciplinas/01-introducao-ao-ciclo-de-vida-de-modelos/temas.md) e [Tech Challenge da Fase 01](../../../../governanca-da-fase/tech-challenge.md).

Esta sequência cobre **5 perguntas operacionais** que todo MLE precisa responder antes de entregar um modelo de churn em produção:

| # | Notebook | Pergunta operacional | Duração-alvo |
|---|----------|----------------------|:------------:|
| 1 | [`01_validacao_pre_treinamento.ipynb`](01_validacao_pre_treinamento.ipynb) | O dado que chegou está pronto para virar treino? | 15 min |
| 2 | [`02_golden_layer_vs_sklearn_pipelines.ipynb`](02_golden_layer_vs_sklearn_pipelines.ipynb) | Onde mexer no dado: antes do treino (medalhão) ou dentro do treino (Pipeline + CV)? | 15 min |
| 3 | [`03_streaming_pipelines_treinamento.ipynb`](03_streaming_pipelines_treinamento.ipynb) | Como treinar quando o dado não cabe na RAM e chega em fluxo contínuo? | 15 min |
| 4 | [`04_profiling_pos_treinamento.ipynb`](04_profiling_pos_treinamento.ipynb) | Como interrogar os splits (treino/teste/holdout) antes de aprovar o modelo? | 15 min |
| 5 | [`05_drift_continuo_e_agentes.ipynb`](05_drift_continuo_e_agentes.ipynb) | Como manter o pipeline vivo com detecção de drift e um agente orquestrando ações? | 15 min |

## Pré-requisitos

- Python 3.10+
- VS Code com extensões `Python` e `Jupyter`
- Setup local conforme o [`README.md` do encontro](../README.md)

## Como rodar

```pwsh
# A partir da raiz do encontro-01
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows
# source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
python dataset\generate_dataset.py     # cria dataset\processed\telco_churn.parquet
jupyter lab notebooks                # ou abra os .ipynb no VS Code
```

> 💡 **Run All habilitado.** Cada notebook executa de cima para baixo sem estado oculto, conforme o [GUIA-007 — Materiais Técnico-Pedagógicos Executáveis](../../../../../../governanca/04-guias/07-guia-de-materiais-tecnico-pedagogicos-executaveis.md).

## Mapa para o Tech Challenge

| Notebook | Tarefa do TC (Etapa 1) | Critério bloqueado se ausente |
|----------|------------------------|-------------------------------|
| 01 | EDA + data readiness | Contrato de dados explícito |
| 02 | Pipeline reprodutível | Sem leakage entre treino/teste |
| 03 | Tracking + dataset version | Histórico auditável de treinos |
| 04 | Métrica técnica + análise por fatia | Model Card preenchida |
| 05 | Plano de monitoramento | Resposta a degradação documentada |

## Notas do condutor

- O encontro tem **60 min**. Use os notebooks como roteiro temporal e abra somente um por vez.
- Os blocos em destaque marcados como `🛑 BREAKPOINT` indicam onde parar para discussão guiada.
- Se algum aluno tiver problema com `river` ou `pandera`, o fallback é executar apenas o caminho pandas + sklearn — todos os notebooks mantêm os trechos canônicos rodando mesmo sem as bibliotecas extras (try/except no setup).
