# Social Media AI Squad for Claude Code

Pacote pronto para operar um squad de IA multi-cliente com contexto isolado por cliente.

## Objetivo

Usar **um único squad padrão** para vários clientes sem misturar contexto.

- O squad é fixo (12 agentes)
- Cada cliente tem pasta própria com memória isolada
- O orquestrador carrega apenas o contexto do cliente informado

## Estrutura rápida

- `MASTER_SYSTEM_PROMPT.md`: prompt mestre para Claude Code
- `ORCHESTRATION_PROTOCOL.md`: protocolo operacional do fluxo
- `CLIENT_FOLDER_STANDARD.md`: padrão de pastas por cliente
- `templates/client_manifest.yaml`: template de cadastro do cliente
- `templates/daily_intel_report.md`: template para agente de inteligência diária
- `templates/weekly_performance_report.md`: template de relatório semanal
- `templates/monthly_strategy_review.md`: template de revisão mensal

## Como usar no dia a dia

1. Criar pasta do cliente em `clientes/<slug-do-cliente>/`
2. Preencher `client_manifest.yaml` com dados da marca
3. Rodar o squad com o comando natural:
   - "Usar cliente: `<slug-do-cliente>`"
4. O Maestro valida contexto e aciona os agentes na ordem correta
5. O agente de inteligência diária roda todos os dias e pode pedir ajustes na estratégia

## Regras de ouro

- Nunca misturar arquivos entre clientes
- Toda recomendação deve citar fonte interna (arquivo + data)
- Toda alteração de estratégia deve gerar log de decisão
- Sem contexto válido de cliente = sem execução
