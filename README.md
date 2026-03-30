# Agente de IA para Estratégia de Social Media

Este repositório define um sistema de **agentes especializados** para montar estratégias de social media com foco em:

- diagnóstico real do mercado;
- análise de concorrentes;
- tendências atuais (com pesquisa na internet);
- recomendações acionáveis com dados e fontes.

## Objetivo

Criar um fluxo onde os agentes:

1. coletam dados públicos e recentes;
2. transformam esses dados em insights estratégicos;
3. convertem os insights em calendário editorial e testes;
4. monitoram resultados e ajustam a estratégia continuamente.

## Estrutura

- `agents/01-pesquisa-mercado.md` — agente que pesquisa nicho, público e tendências.
- `agents/02-inteligencia-competitiva.md` — agente que analisa concorrentes e benchmarks.
- `agents/03-estrategia-editorial.md` — agente que gera pilares, ângulos e calendário.
- `agents/04-copiloto-metricas.md` — agente que mede performance e propõe otimizações.
- `playbooks/briefing-cliente.md` — formulário de onboarding para alimentar os agentes.
- `playbooks/protocolo-qualidade.md` — critérios para evitar “balela” e garantir dados reais.
- `playbooks/modelagem-custos.md` — guia para escolher modelo e controlar custos de créditos.
- `playbooks/briefing-exemplo.json` — briefing pronto para teste rápido.
- `scripts/run_agents.py` — script para gerar prompts executáveis para cada agente.

## Online ou local: qual usar?

- **Online (ChatGPT Web/Desktop)**: melhor para começar rápido. Você gera o prompt e cola no chat.
- **Local (terminal + script)**: melhor para padronizar, versionar e escalar para vários clientes.
- **Produção (API + automação)**: melhor para operação semanal com menos trabalho manual.

### Recomendação prática

1. Comece com **ChatGPT Desktop/Web** para validar o método.
2. Depois passe para **terminal + script** quando quiser repetibilidade.
3. Por fim, conecte em **API + n8n/Make** para operação contínua.

## Como rodar no ChatGPT Desktop (passo a passo)

1. No terminal, execute:

```bash
python3 scripts/run_agents.py --agent 01 --print
```

2. Copie o prompt que apareceu no terminal (ou abra o arquivo em `outputs/`).
3. Cole no ChatGPT Desktop/Web.
4. Anexe dados extras (prints de métricas, planilha, links de concorrentes).
5. Peça explicitamente: "use fontes recentes e cite data e link em cada insight".

> Sim: você consegue usar esses agentes no app desktop do ChatGPT sem problema.

## Como rodar via terminal

### Gerar todos os agentes

```bash
python3 scripts/run_agents.py --agent all
```

### Gerar um agente e imprimir no terminal

```bash
python3 scripts/run_agents.py --agent 02 --print
```

### Salvar em outra pasta

```bash
python3 scripts/run_agents.py --agent all --output-dir ./meus-prompts
```





## Qual modelo usar sem gastar todos os créditos?

Use a estratégia em camadas:

1. **mini/rápido** para rascunho e volume.
2. **intermediário** para análise e priorização.
3. **top-tier** só na versão final para cliente.

Guia completo: `playbooks/modelagem-custos.md`.

## Depois de subir no GitHub: como baixar

### Opção 1 (mais fácil, sem terminal)
1. Abra o repositório no GitHub.
2. Clique em **Code**.
3. Clique em **Download ZIP**.

### Opção 2 (via terminal)
```bash
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_REPO>
make zip
```

Isso vai gerar o arquivo `dist/agentes-social-media.zip` localmente.

## Botão de baixar tudo (como funciona)

Se você estiver no **GitHub**, o botão é:

1. Clique em **Code**
2. Clique em **Download ZIP**

Se estiver rodando local no terminal, o equivalente ao “botão” é:

```bash
make zip
```

Isso gera `dist/agentes-social-media.zip` localmente (o `.zip` não é versionado no Git).

## Exportar tudo em um ZIP (1 arquivo só)

Para empacotar tudo e enviar para outra IA ler de uma vez:

```bash
python3 scripts/build_zip.py
```

Arquivo gerado:

- `dist/agentes-social-media.zip` (gerado localmente)

Você pode descompactar esse `.zip` e apontar a pasta inteira para a IA.

## Fluxo recomendado (operacional)

1. Preencha o briefing do cliente em `playbooks/briefing-cliente.md`.
2. Rode o Agente 01 para mapear cenário e oportunidades.
3. Rode o Agente 02 para comparar com concorrentes.
4. Rode o Agente 03 para construir plano de conteúdo por 30 dias.
5. Rode o Agente 04 semanalmente para revisar métricas e ajustar.
6. Valide tudo com o protocolo em `playbooks/protocolo-qualidade.md`.

## Regras de qualidade

- Toda recomendação deve incluir: **dado + interpretação + ação**.
- Toda afirmação factual deve incluir **fonte e data**.
- Evitar “achismos”: quando não houver dado suficiente, marcar como hipótese.
