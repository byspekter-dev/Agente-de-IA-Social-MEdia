#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

FILES_TO_PACKAGE = [
    "README.md",
    ".gitignore",
    "agents/01-pesquisa-mercado.md",
    "agents/02-inteligencia-competitiva.md",
    "agents/03-estrategia-editorial.md",
    "agents/04-copiloto-metricas.md",
    "playbooks/briefing-cliente.md",
    "playbooks/briefing-exemplo.json",
    "playbooks/protocolo-qualidade.md",
    "scripts/run_agents.py",
    "scripts/build_zip.py",
    "Makefile",
]

OUTPUT_ZIP = Path("dist/agentes-social-media.zip")


def main() -> None:
    OUTPUT_ZIP.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(OUTPUT_ZIP, "w", compression=ZIP_DEFLATED) as zipf:
        for file_rel in FILES_TO_PACKAGE:
            path = Path(file_rel)
            if not path.exists():
                raise FileNotFoundError(f"Arquivo não encontrado para empacotar: {file_rel}")
            zipf.write(path, arcname=file_rel)

    print(f"[ok] ZIP criado em: {OUTPUT_ZIP}")
    print("[ok] Arquivos incluídos:")
    for file_rel in FILES_TO_PACKAGE:
        print(f" - {file_rel}")


if __name__ == "__main__":
    main()
