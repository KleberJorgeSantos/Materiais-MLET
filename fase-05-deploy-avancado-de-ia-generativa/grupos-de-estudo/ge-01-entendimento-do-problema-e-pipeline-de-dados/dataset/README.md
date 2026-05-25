# Data

Esta pasta hospeda os artefatos de dados usados pelos notebooks do Encontro 01.

```
data/
├── README.md
├── generate_dataset.py     ← script único de geração (Telco churn sintético)
├── raw/                    ← saída do estágio Bronze
├── interim/                ← saída do estágio Silver
└── processed/              ← saída do estágio Gold (telco_churn.parquet)
```

## Como gerar os dados

```pwsh
python dataset\generate_dataset.py
```

O script é determinístico (`seed=42`) e produz aproximadamente 8.000 clientes com 19 features mistas (numéricas, categóricas, booleanas) e uma coluna alvo `churn`.

A partir do estágio Gold, todos os notebooks da pasta `notebooks/` podem ser executados sem dependência externa.

> ⚠️ Os arquivos sob `raw/`, `interim/` e `processed/` ficam ignorados por Git (`.gitignore` do repositório raiz). Recrie-os com o script sempre que precisar de um dataset limpo.
