# Padrão de Pastas por Cliente

Use este padrão para cada cliente:

```txt
clientes/<slug-cliente>/
  00_onboarding/
    client_manifest.yaml
  01_diagnostico/
    latest_diagnosis.md
  02_mercado-concorrentes/
    benchmark.md
    daily/
      YYYY-MM-DD.md
  03_estrategia/
    current_strategy.md
    change_log/
      YYYY-MM-DD-<motivo>.md
  04_calendario/
    editorial_calendar.csv
  05_producao/
    briefs/
    copies/
    assets_requests/
  06_publicado/
    published_log.csv
  07_metricas/
    latest_metrics_snapshot.csv
    weekly/
      YYYY-Www.md
    monthly/
      YYYY-MM.md
  08_experimentos/
    backlog.md
    tests_log.csv
  09_relatorios/
    weekly_report.md
    monthly_review.md
```

## Arquivos mínimos obrigatórios

- `00_onboarding/client_manifest.yaml`
- `03_estrategia/current_strategy.md`
- `07_metricas/latest_metrics_snapshot.csv`

Sem eles, o squad deve operar em modo diagnóstico/pêndencia, sem publicação.
