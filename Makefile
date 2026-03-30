.PHONY: help prompts zip route auto

help:
	@echo "Comandos disponíveis:"
	@echo "  make prompts   # gera prompts dos 4 agentes em outputs/"
	@echo "  make zip       # gera dist/agentes-social-media.zip"
	@echo "  make route     # recomenda modelo por agente/etapa"
	@echo "  make auto      # gera tudo automaticamente (prompts + plano + zip)"

prompts:
	python3 scripts/run_agents.py --agent all

zip:
	python3 scripts/build_zip.py

route:
	python3 scripts/model_router.py --agent all --stage analise

auto:
	python3 scripts/auto_pipeline.py --stage analise --zip
