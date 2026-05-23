# Changelog

## 2026-05-22

- Adicionado o pacote público do Datathon 7-MLET em `fase-05-deploy-avancado-de-ia-generativa/datathon/7mlet/`, com o desafio financeiro sanitizado de experimentação adaptativa em ofertas.
- Complementado o pacote 7-MLET com critério obrigatório de arquitetura-alvo em Azure, diagramas Mermaid do fluxo da aplicação, estrutura esperada de repositório e exemplos didáticos de código.
- Substituída a obrigatoriedade de um dataset único por orientação de bases Kaggle compatíveis e instruções para criação de datasets derivados, com enriquecimento sintético documentado para braços de decisão, recompensas e eventos atrasados.
- Reestruturada a seção de entregáveis obrigatórios do Datathon 7-MLET como listagem extensa por etapa (0 a 8), com objetivo, sub-bullets técnicos detalhados e critério de evidência de aceite em cada etapa; a matriz tabular anterior foi absorvida nesta listagem.
- Movida a seção "Entregáveis obrigatórios" para o final do arquivo, depois de "Proveniência e revisão", para funcionar como referência de fechamento que os grupos consultam antes da submissão.
- Incluída subseção "Critérios de apresentação" cobrindo FinOps (ROI, custo, TCO), arquitetura técnica e cenários de escala e redução por volume de requisições; checklist do Demo Day e Etapa 8 da listagem de entregáveis alinhados para exigir cobertura explícita dessas dimensões no pitch.
- Marcada a demonstração ao vivo ou gravada da plataforma durante o pitch como desejável e bonificada com pontos extras, com nota correspondente na subseção "Critérios de apresentação", item adicional no checklist do Demo Day e bullet específico na Etapa 8 da listagem de entregáveis (incluindo exigência de plano de contingência).
- Adicionada seção "Objetivo final — uma plataforma que aprende de forma automática" contrastando teste A/B (Cientista de Dados decide) com Multi-Armed Bandits (o sistema identifica a melhor ação) e listando o que a banca observa para considerar a entrega como plataforma de aprendizado contínuo.
- Adicionadas referências algorítmicas a Thompson Sampling e Nilos-UCB, exemplo financeiro de inferência contextual e exigência de camada de retreino, aprovação e gestão do ciclo de vida de políticas adaptativas.
- Criado o índice local de Datathon da Fase 05 em `fase-05-deploy-avancado-de-ia-generativa/datathon/README.md`.
- Atualizados os indicadores públicos de cobertura da MLET7 e o README da Fase 05 para apontar para o novo pacote.
- Reestruturado o README do Datathon 7-MLET espelhando edições estruturais aplicadas pela equipe de plataforma no `.docx`: a seção "Desafio único — Experimentação Adaptativa em Ofertas Financeiras" foi renomeada para "Experimentação Adaptativa em Ofertas Financeiras" e promovida para logo após "Visão geral"; a subseção "Escopo técnico" foi reparentada para dentro de "Bases Kaggle orientadoras e criação dos datasets"; "Objetivo final" passou a usar dois-pontos em vez de em-dash; a seção "Conexão com os grupos de estudo" foi removida; a ordem da metade inferior passou a ser Objetivo final → Proveniência e revisão → Entregáveis obrigatórios → Critérios de avaliação → Checklist antes do Demo Day (última), substituindo a ordem anterior em que "Entregáveis obrigatórios" fechava o documento.
- Publicado `fase-05-deploy-avancado-de-ia-generativa/datathon/7mlet/README.docx` co-localizado com o `README.md`, seguindo o padrão do pacote 6-MLET (`datathon/6mlet/README.md` + `README.docx`), gerado a partir do `README.md` para garantir paridade estrutural entre as duas representações.

## 2026-05-07

- Adicionados 56 scripts Python completos e executáveis para apoiar lives técnicas, grupos de estudo e lives de grupos de estudo:
  - 16 scripts `exercicio.py` para lives técnicas, com cenários de engenharia de ML, gates, riscos, evidências e referências por tema.
  - 20 scripts `apoio_estudo.py` para grupos de estudo, com matriz de decisão, evidências esperadas e conexão com o Tech Challenge.
  - 20 scripts `apoio_live.py` para lives de grupos de estudo, com ações de follow-up, critérios de aceite e referências.
  - Todos usam apenas biblioteca padrão do Python e possuem modo `--check`.
- Atualizado `docs/live-study-artifact-inventory.md` para refletir a cobertura dos scripts Python.
- Gerados artefatos de acompanhamento em nível de engenharia de machine learning para todas as pastas de lives e grupos de estudo, com inventário central em `docs/live-study-artifact-inventory.md`.
- Promoted `CONTRIBUTING.md` and `CHANGELOG.md` to the repository root to match public GitHub conventions.
- Added a documentation index in `docs/README.md` so students do not land on an unstructured folder listing.
- Documented the complementary `fase-04-validacao-de-dados/` folder with a local README and pointers back to the canonical Phase 04 discipline path.

## 2026-05-06

- Removed student-facing exposure of repository agent customization, test harness, tool scripts, and root validation shortcuts from the current tree.
- Kept detailed navigation and coverage notes in `docs/`; root contribution and changelog files now follow GitHub conventions.
- Moved live-session and study-group materials into phase-local paths.
- Kept cross-cohort coverage and index documents in `docs/`.
