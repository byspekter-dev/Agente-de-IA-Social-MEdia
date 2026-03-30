#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from model_router import recommend
from run_agents import build_prompt, load_text

AGENTS = {
    "01": "agents/01-pesquisa-mercado.md",
    "02": "agents/02-inteligencia-competitiva.md",
    "03": "agents/03-estrategia-editorial.md",
    "04": "agents/04-copiloto-metricas.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Pipeline automático: roteia modelo, gera prompts dos 4 agentes e empacota resultados."
    )
    parser.add_argument("--briefing", default="playbooks/briefing-exemplo.json")
    parser.add_argument("--stage", choices=["rascunho", "analise", "final"], default="analise")
    parser.add_argument("--output-dir", default="outputs")
    parser.add_argument("--zip", action="store_true", help="Gera ZIP com prompts e plano de execução.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    briefing = json.loads(load_text(Path(args.briefing)))

    plan: list[dict[str, str]] = []
    files_for_zip: list[Path] = []

    for agent_id, agent_file in AGENTS.items():
        model = recommend(agent_id, args.stage)
        agent_md = load_text(Path(agent_file))
        prompt = build_prompt(agent_md, briefing)

        prompt_path = output_dir / f"agent-{agent_id}-{ts}.md"
        prompt_path.write_text(prompt, encoding="utf-8")

        plan.append(
            {
                "agent": agent_id,
                "stage": args.stage,
                "model_recomendado": model,
                "prompt_file": str(prompt_path),
            }
        )
        files_for_zip.append(prompt_path)

    plan_path = output_dir / f"plano-execucao-{ts}.json"
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    files_for_zip.append(plan_path)

    print(f"[ok] Plano automático gerado: {plan_path}")
    for item in plan:
        print(
            f"[ok] Agente {item['agent']} | modelo: {item['model_recomendado']} | prompt: {item['prompt_file']}"
        )

    if args.zip:
        zip_path = output_dir / f"lote-agentes-{ts}.zip"
        with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as zipf:
            for file in files_for_zip:
                zipf.write(file, arcname=file.name)
        print(f"[ok] ZIP de execução gerado: {zip_path}")


if __name__ == "__main__":
    main()
