# 📖 Grupo de Estudos 1 — Entendimento do Problema e Pipeline de Dados

> **Fase:** 05 — Deploy Avançado de IA Generativa | **Etapa do TC:** 1
> **Integra:** Fase 01 (EDA, baselines) + Fase 02 (versionamento, Docker) + Briefing da empresa

---

## 📋 Foco da Sessão

Análise do problema real fornecido pela empresa convidada, exploração de dados e construção de pipeline reprodutível.

**Disciplinas de referência:**
- [`01-deploy-modelos-ia-generativa`](../../01-deploy-modelos-ia-generativa/)
- Competências acumuladas de Fases 01 e 02

---

## 🎯 Objetivos

- Analisar dados da empresa: EDA completa com insights relevantes
- Treinar baseline preditivo (Scikit-Learn + MLP PyTorch)
- Construir pipeline reprodutível (Docker + DVC + MLflow)
- Definir métricas alinhadas ao negócio (traduzir KPIs da empresa)
- Produzir relatório de viabilidade (≤ 2 páginas)

---

## 🗂️ Roteiro de Discussão

### 1. Revisão Conceitual (~20 min)

- Como abordar um problema "do mundo real" vs. acadêmico?
- Traduzir requisitos de negócio em métricas técnicas
- Pipeline de dados: ingestão → limpeza → feature engineering → versionamento
- Relatório de viabilidade: o que incluir para stakeholders não-técnicos

### 2. Exercício Guiado (~40 min)

1. **Análise do briefing da empresa:**
   - Qual o problema? Quem é impactado?
   - Quais dados foram fornecidos? Formatos, volumes, qualidade
   - KPIs de negócio definidos pela empresa
   - Restrições: latência, privacidade, custo

2. **EDA orientada ao negócio:**
   - Não apenas descrever dados, mas gerar insights actionable
   - Quais features parecem mais relevantes para o KPI?
   - Missing values: impacto nas métricas? Estratégia de imputação?
   - Visualizações que comunicam para a empresa

3. **Pipeline reprodutível:**
   - Docker para ambiente isolado
   - DVC para versionar dados da empresa
   - MLflow para tracking desde o primeiro experimento
   - `dvc repro` funciona em qualquer máquina

4. **Baseline + métricas:**
   - Modelo simples (LogReg, XGBoost) como referência
   - Mapear KPI da empresa → métrica técnica (ex.: "reduzir análise em 40%" → recall mínimo)
   - Documentar: baseline atinge ou não os critérios da empresa?

### 3. Discussão Aberta (~20 min)

- Como lidar com dados "sujos" fornecidos pela empresa?
- NDA e dados sensíveis: cuidados com versionamento
- Quando os critérios da empresa são impossíveis: como comunicar?
- Estratégia de divisão de trabalho no grupo para as 4 etapas

### 4. Conexão com Tech Challenge (~10 min)

**Critérios de aceite da Etapa 1:**

- [ ] EDA documentada com insights relevantes para o problema da empresa
- [ ] Baseline treinado e métricas reportadas (comparadas com KPIs da empresa)
- [ ] Pipeline versionado (DVC + Docker) e reprodutível
- [ ] Métricas de negócio mapeadas para métricas técnicas
- [ ] Relatório de viabilidade (≤ 2 páginas)

---

## 📚 Referências

- Material da disciplina: [`01-deploy-modelos-ia-generativa`](../../01-deploy-modelos-ia-generativa/)
- Competências de Fase 01: EDA, ML Canvas, baselines, MLflow
- Competências de Fase 02: Docker, DVC, Poetry, clean code

## Artefatos de acompanhamento

- [Guia de estudo](guia-de-estudo.md)
- [Atividade do aluno](atividade-do-aluno.md)
- [Checklist tech challenge](checklist-tech-challenge.md)
- [Script Python de apoio](apoio_estudo.py)
- [Notebooks práticos](notebooks/README.md) — 5 notebooks executáveis cobrindo o ciclo "Entendimento do Problema → Pipeline de Dados"
- [Gerador de dataset sintético](dataset/README.md) — Telco churn determinístico (seed=42, 8 000 linhas)
- [`requirements.txt`](requirements.txt) — dependências fixadas para o venv do encontro

---

## 🧪 Notebooks Práticos

Os notebooks abaixo materializam o roteiro do encontro com um dataset sintético de **Telco churn** (gerado pelo script em [`dataset/generate_dataset.py`](dataset/generate_dataset.py)). Servem como **espinha técnica** para a Etapa 1 do Tech Challenge: cada notebook entrega um critério de aceite reproduzível.

| # | Notebook | O que entrega | Item do checklist |
|---|----------|---------------|-------------------|
| 1 | [`01_validacao_pre_treinamento.ipynb`](notebooks/01_validacao_pre_treinamento.ipynb) | Contrato `pandera` (21 colunas), readiness report e veredito GO/NO-GO em JSON | EDA documentada + pipeline reprodutível |
| 2 | [`02_golden_layer_vs_sklearn_pipelines.ipynb`](notebooks/02_golden_layer_vs_sklearn_pipelines.ipynb) | Medalhão (Bronze→Silver→Gold) × `sklearn.Pipeline` + `StratifiedKFold` + anti-pattern de *leakage* | Pipeline versionado e separação exploração/execução |
| 3 | [`03_streaming_pipelines_treinamento.ipynb`](notebooks/03_streaming_pipelines_treinamento.ipynb) | Treino *out-of-core* com `SGDClassifier.partial_fit` + `river` online + tracking MLflow | Baseline treinado + tracking desde o primeiro experimento |
| 4 | [`04_profiling_pos_treinamento.ipynb`](notebooks/04_profiling_pos_treinamento.ipynb) | Split 70/15/15, PSI, *learning curve*, *slice metrics*, esboço de Model Card | Métricas mapeadas a KPIs e relatório de viabilidade |
| 5 | [`05_drift_continuo_e_agentes.ipynb`](notebooks/05_drift_continuo_e_agentes.ipynb) | Drift contínuo (PSI + KS), agente ReAct com `TOOLS` dict, *ledger* JSON-lines e stub LLM | Próximo passo (operação) já antecipado para a Fase 05 |

**Receita de execução** (Python 3.13, qualquer SO):

```bash
python -m venv .venv
.venv\Scripts\activate                     # PowerShell
# OU
source .venv/bin/activate                  # bash/zsh

pip install -r requirements.txt
python -m ipykernel install --user --name encontro01 --display-name "Python (encontro-01)"

python dataset/generate_dataset.py         # gera dataset/processed/telco_churn.{parquet,csv}
jupyter lab notebooks                      # Run All em cada notebook
```

> **Conexão com Fase 05:** o exemplo é supervisionado clássico (churn), mas as práticas — contrato de schema, pipeline single-source, profiling por *slice*, drift contínuo, agente orquestrador — transferem para o cenário generativo da Fase 05. Os notebooks 4 e 5 já preparam o vocabulário (Model Card, ledger de decisões, tools dict) que será usado nas próximas etapas com LLMs e RAG.
