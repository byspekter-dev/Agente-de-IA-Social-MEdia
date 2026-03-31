# Orchestration Protocol (Multi-Cliente)

## 1) Handshake inicial

- Receber: `cliente_slug`, objetivo, prazo, canal
- Validar existência da pasta `clientes/<cliente_slug>/`
- Validar arquivos obrigatórios

Se qualquer validação falhar:
- Registrar pendência
- Sugerir próximo passo
- Não inventar dados

## 2) Pipeline padrão

1. Diagnóstico (se novo cliente ou estratégia desatualizada)
2. Daily Intel (sempre)
3. Estratégia (macro ou ajuste)
4. Calendário
5. Copy
6. Briefing criativo
7. QA + aprovação
8. Produção final
9. Programação
10. Analytics
11. Experimentos

## 3) Regra do Daily Intel

Rodar diariamente e produzir:
- Mudanças do nicho
- Movimentos de concorrentes
- Tendências novas
- Oportunidades acionáveis (top 3)
- Recomendações de ajuste (baixo, médio, alto impacto)

Saída obrigatória: `02_mercado-concorrentes/daily/YYYY-MM-DD.md`

## 4) Regras de alteração estratégica

A estratégia só muda quando houver pelo menos 1:
- Tendência sustentada por mais de 3 dias
- Queda relevante de KPI principal por 2 janelas seguidas
- Mudança de produto/oferta do cliente

Toda alteração deve gerar:
- `03_estrategia/change_log/YYYY-MM-DD-<motivo>.md`

## 5) Governança de aprovação

Sem aprovação explícita:
- Não publicar

Checklist mínimo:
- Tom de voz correto
- CTA claro
- Conformidade de marca
- Links e UTMs validados
- Formato correto por canal

## 6) Ritmo de operação

- Diário: Daily Intel + execução
- Semanal: revisão tática
- Mensal: revisão estratégica

## 7) Saída padrão do Maestro

Sempre entregar:
1. Status atual
2. O que mudou
3. O que será executado hoje
4. Bloqueios
5. Decisões necessárias do cliente
