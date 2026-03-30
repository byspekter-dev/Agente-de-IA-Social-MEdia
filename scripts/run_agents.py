#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

AGENTS = {
    "01": "agents/01-pesquisa-mercado.md",
    "02": "agents/02-inteligencia-competitiva.md",
    "03": "agents/03-estrategia-editorial.md",
    "04": "agents/04-copiloto-metricas.md",
}


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def build_prompt(agent_md: str, briefing: dict) -> str:
    briefing_json = json.dumps(briefing, ensure_ascii=False, indent=2)
    return (
        "Você é um agente especialista de social media. "
        "Use somente dados verificáveis, cite fonte e data, e nunca invente números.\n\n"
        "## Briefing do cliente\n"
        f"{briefing_json}\n\n"
        "## Instruções do agente\n"
        f"{agent_md}\n\n"
        "## Formato obrigatório de resposta\n"
        "1) Diagnóstico baseado em evidências\n"
        "2) Recomendações priorizadas (alto/médio/baixo impacto)\n"
        "3) Plano de execução da semana\n"
        "4) Riscos, lacunas e hipóteses\n"
        "5) Fontes consultadas com data\n"
    )


def save_output(agent_id: str, prompt: str, output_dir: Path) -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"agent-{agent_id}-{ts}.md"
    output_path.write_text(prompt, encoding="utf-8")
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gera prompts prontos para testar os agentes de social media."
    )
    parser.add_argument(
        "--agent",
        choices=["01", "02", "03", "04", "all"],
        default="all",
        help="Qual agente executar. Use 'all' para gerar os 4 prompts.",
    )
    parser.add_argument(
        "--briefing",
        default="playbooks/briefing-exemplo.json",
        help="Caminho para briefing em JSON.",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Pasta onde os prompts gerados serão salvos.",
    )
    parser.add_argument(
        "--print",
        action="store_true",
        help="Também imprime o prompt no terminal para copiar e colar no ChatGPT.",
    )
    return parser.parse_args()


def run_agent(agent_id: str, briefing: dict, output_dir: Path, print_prompt: bool) -> Path:
    agent_path = Path(AGENTS[agent_id])
    agent_md = load_text(agent_path)
    prompt = build_prompt(agent_md, briefing)
    output_path = save_output(agent_id, prompt, output_dir)
    print(f"[ok] Prompt do agente {agent_id} salvo em: {output_path}")

    if print_prompt:
        print("\n" + "=" * 80)
        print(f"PROMPT AGENTE {agent_id}")
        print("=" * 80)
        print(prompt)

    return output_path


def main() -> None:
    args = parse_args()
    briefing_path = Path(args.briefing)
    output_dir = Path(args.output_dir)
    briefing = json.loads(load_text(briefing_path))

    if args.agent == "all":
        for agent_id in ["01", "02", "03", "04"]:
            run_agent(agent_id, briefing, output_dir, args.print)
        return

    run_agent(args.agent, briefing, output_dir, args.print)


if __name__ == "__main__":
    main()
