.PHONY: help install demo test clean

help:
	@echo "Targets: install | demo | clean"

install:
	pip install -e .

demo:
	rm -f audit.log
	python -m azure_ops_mcp kv-compare fixtures/vaults/dev-vault.json fixtures/vaults/prod-vault.json >/tmp/ops-kv.json
	python -m azure_ops_mcp ado-diagnose fixtures/ado/failed-job.json >/tmp/ops-ado.json
	python -m azure_ops_mcp cost-stub fixtures/cost/sample-costs.json >/tmp/ops-cost.json
	@test -f audit.log
	@echo "✓ azure-ops-mcp demo OK — tools ran dry-run; audit.log written" 

clean:
	rm -rf .venv dist build *.egg-info reports labs out audit.log __pycache__
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
