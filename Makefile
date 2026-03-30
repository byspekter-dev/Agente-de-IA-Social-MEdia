.PHONY: help prompts zip

help:
	@echo "Comandos disponíveis:"
	@echo "  make prompts   # gera prompts dos 4 agentes em outputs/"
	@echo "  make zip       # gera dist/agentes-social-media.zip"

prompts:
	python3 scripts/run_agents.py --agent all

zip:
	python3 scripts/build_zip.py
