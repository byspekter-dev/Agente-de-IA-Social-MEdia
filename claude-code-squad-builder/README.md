# Squad Builder AI for Claude Code

Pacote separado para criar squads de IA para qualquer serviço, sem misturar com o pacote de social media.

## Objetivo

Receber um pedido de negócio (ex.: "quero um squad para suporte", "quero um squad para vendas") e gerar um squad operacional completo:

- agentes
- workflow
- prompts
- templates
- governança
- KPIs

## Arquivos

- `MASTER_SYSTEM_PROMPT.md`: prompt mestre do Squad Builder
- `ORCHESTRATION_PROTOCOL.md`: protocolo operacional para criação do squad
- `DISCOVERY_QUESTION_FLOW.md`: árvore de perguntas inteligentes
- `AGENTS_MATRIX.md`: funções dos agentes do Squad Builder
- `OUTPUT_SPEC.md`: formato padrão de saída final
- `templates/intake_form.yaml`: template de coleta inicial
- `templates/squad_blueprint.md`: template do blueprint final
- `templates/agent_card.md`: template de ficha por agente

## Uso rápido

1. Abra esta pasta no Claude Code.
2. Peça para ler os arquivos centrais.
3. Informe o serviço alvo.
4. Responda as perguntas de discovery.
5. Aprove a versão do blueprint.
6. Receba o squad pronto para operação.

## Regra de separação

Este pacote não deve alterar nem depender da pasta `claude-code-social-squad/`.
