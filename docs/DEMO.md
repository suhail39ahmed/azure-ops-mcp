# Demo — azure-ops-mcp

Loom / screen recording script (**60–90 seconds**). Speak calmly; show the terminal, not slides.

## Setup (before record)

```bash
cd azure-ops-mcp
python -m venv .venv && source .venv/bin/activate
pip install -e .
# clear scrollback; font size ~16–18pt; dark theme
```

## Exact click / type script

1. Open terminal at repo root. Say: *"This is azure-ops-mcp — Azure ops tools for agents: Key Vault compare, ADO diagnose, cost stub — dry-run…"*
2. Type `make demo` **or** walk the commands below one by one.
1. Run `python -m azure_ops_mcp --help` — wait for JSON / output.
2. Run `python -m azure_ops_mcp kv-compare fixtures/vaults/dev-vault.json fixtures/vaults/prod-vault.json` — wait for JSON / output.
3. Run `python -m azure_ops_mcp ado-diagnose fixtures/ado/failed-job.json` — wait for JSON / output.
4. Run `python -m azure_ops_mcp cost-stub fixtures/cost/sample-costs.json` — wait for JSON / output.
3. Scroll the JSON briefly. Call out one concrete field (citation path, `human_approval_required`, findings, report path, etc.).
4. Close with: *"Offline fixtures only — clone it, `make demo`, adopt the pattern."* Link the GitHub repo in the Loom description.

## Talking points (pick 2)

- Who it's for: Azure platform SAs building agent tools that must stay auditable.
- What it is NOT: Not a replacement for Azure Portal / Cost Management
- Honest MVP: no fabricated production metrics

## Outro card (last 3s)

`github.com/suhail39ahmed/azure-ops-mcp`
