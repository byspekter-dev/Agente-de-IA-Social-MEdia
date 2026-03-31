# Orchestration Protocol - Squad Builder

## Etapa 1: Intake

- Ler `templates/intake_form.yaml`
- Coletar respostas mínimas do usuário
- Validar suficiência

## Etapa 2: Arquitetura

- Definir número de agentes
- Definir responsabilidade de cada agente
- Definir handoff entre agentes

## Etapa 3: Workflow

- Definir pipeline ponta a ponta
- Definir pontos de QA
- Definir pontos de aprovação humana

## Etapa 4: Governança

- Definir regras de bloqueio
- Definir critérios de exceção
- Definir logs obrigatórios

## Etapa 5: Métricas

- Definir north-star metric
- Definir KPIs primários/secundários
- Definir cadência de revisão

## Etapa 6: Entrega

Entregar usando `OUTPUT_SPEC.md` + templates:
- `templates/squad_blueprint.md`
- `templates/agent_card.md`

## Etapa 7: Simulação mínima

Rodar simulação de 3 cenários:
1. Cenário normal
2. Cenário de falha operacional
3. Cenário de mudança de prioridade

Ajustar blueprint conforme achados.
