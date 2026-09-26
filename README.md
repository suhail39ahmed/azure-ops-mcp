# azure-ops-mcp

MCP-shaped Azure ops tools: **kv_compare**, **ado_diagnose**, **cost_stub**. Dry-run default + append-only audit log. Fixture JSON only — **no live Azure calls** required for demos.

## What it is
- Offline ops toolkit for agents / CLI
- Compares Key Vault config fixtures, diagnoses ADO failure fixtures, stubs cost rollups

## What it is not
- Not a replacement for Azure Portal / Cost Management
- Not granted production RBAC in this repo

## Architecture

```
  CLI / Agent
      |
      v
  tools (dry-run) --> fixtures/*.json
      |
      +--> audit.log (append JSON lines)
```

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m azure_ops_mcp.cli kv-compare fixtures/vaults/dev-vault.json fixtures/vaults/prod-vault.json
python -m azure_ops_mcp.cli ado-diagnose fixtures/ado/failed-job.json
python -m azure_ops_mcp.cli cost-stub fixtures/cost/sample-costs.json
cat audit.log
```

## Demo assets checklist
- [ ] `assets/demo.gif`
- [ ] `assets/architecture.png`
- [ ] `docs/DEMO.md`

## License
MIT
