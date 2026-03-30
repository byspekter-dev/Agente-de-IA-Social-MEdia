.PHONY: help prompts zip route

help:
	@echo "Comandos disponíveis:"
	@echo "  make prompts   # gera prompts dos 4 agentes em outputs/"
	@echo "  make zip       # gera dist/agentes-social-media.zip"
	@echo "  make route     # recomenda modelo por agente/etapa"

prompts:
	python3 scripts/run_agents.py --agent all

zip:
	python3 scripts/build_zip.py

route:
	python3 scripts/model_router.py --agent all --stage analise
