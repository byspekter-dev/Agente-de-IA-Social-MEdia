# Modelos recomendados (qualidade x custo)

## Regra prática (sem gastar tudo de uma vez)

- **Rascunho e volume** (ideias, variações, calendário base): use modelo **mini/rápido**.
- **Análise estratégica** (priorização, diagnóstico, decisão): use modelo **intermediário**.
- **Entrega final crítica** (plano final para cliente): use modelo **top-tier** apenas no fechamento.

## Roteamento sugerido por agente

1. **Agente 01 — Pesquisa de mercado**
   - Coleta inicial: mini/rápido.
   - Síntese final com fontes: intermediário.

2. **Agente 02 — Inteligência competitiva**
   - Extração de padrões: mini/rápido.
   - Matriz de diferenciação: intermediário.

3. **Agente 03 — Estratégia editorial**
   - Geração de calendário: mini/rápido.
   - Revisão de coerência e posicionamento: intermediário.

4. **Agente 04 — Métricas e otimização**
   - Leitura semanal: mini/rápido.
   - Diagnóstico de causa-raiz: intermediário (ou top-tier em contas grandes).

## Regras de economia (importante)

- Defina limite de rodadas por agente (ex.: no máximo 2 iterações).
- Use prompt objetivo e estruturado (evita respostas longas desnecessárias).
- Reaproveite contexto fixo do cliente (não reescrever tudo em toda chamada).
- Faça "escada de qualidade": mini -> intermediário -> top-tier só no final.
- Para cliente pequeno, normalmente **mini + intermediário** já resolve.

## Configuração inicial recomendada

- 70% das execuções em mini/rápido.
- 25% em intermediário.
- 5% em top-tier (somente revisão final / casos críticos).

## Dica operacional no Codex/terminal

- Comece testando com mini/rápido para validar fluxo.
- Troque para intermediário quando a resposta exigir mais profundidade.
- Use top-tier apenas para entregar material final ao cliente.
