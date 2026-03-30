#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json

BASE_BY_STAGE = {
    "rascunho": "mini/rápido",
    "analise": "intermediário",
    "final": "top-tier",
}

AGENT_OVERRIDES = {
    "01": {"final": "intermediário"},
    "02": {"final": "intermediário"},
    "03": {"final": "intermediário"},
    "04": {"final": "intermediário (top-tier apenas em conta grande)"},
}


def recommend(agent: str, stage: str) -> str:
    default_model = BASE_BY_STAGE[stage]
    return AGENT_OVERRIDES.get(agent, {}).get(stage, default_model)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Recomenda o nível de modelo para cada agente sem estourar créditos."
    )
    parser.add_argument("--agent", choices=["01", "02", "03", "04", "all"], default="all")
    parser.add_argument(
        "--stage",
        choices=["rascunho", "analise", "final"],
        default="analise",
        help="Etapa do trabalho.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Retorna em JSON para integrar em automações.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    agents = ["01", "02", "03", "04"] if args.agent == "all" else [args.agent]

    data = {agent: recommend(agent, args.stage) for agent in agents}

    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return

    print(f"Etapa: {args.stage}")
    for agent, model in data.items():
        print(f"Agente {agent}: {model}")


if __name__ == "__main__":
    main()
