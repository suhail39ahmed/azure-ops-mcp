# Demo — azure-ops-mcp

Honest, fixture-only demos. No fabricated metrics.

## Timed Loom (60–90s)

| Time | On screen | Say |
|------|-----------|-----|
| 0:00–0:10 | Repo root | "Azure ops tools for agents — dry-run default + append-only audit log." |
| 0:10–0:50 | Primary command | Walk the happy path; call out one concrete field or file. |
| 0:50–1:15 | Second beat | Show the punchline artifact. |
| 1:15–1:30 | Outro card | "Offline fixtures — clone it, make demo." |

### Exact commands

```bash
cd azure-ops-mcp
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m azure_ops_mcp kv-compare fixtures/vaults/dev-vault.json fixtures/vaults/prod-vault.json
cat audit.log
make demo
```

### Shot list (3 frames)

1. Primary command output  
2. Punchline artifact (report / audit / SQL / lab tree)  
3. `make demo` success line  

### Outro card

`github.com/suhail39ahmed/azure-ops-mcp`

## LinkedIn first-comment

```
git clone https://github.com/suhail39ahmed/azure-ops-mcp.git
cd azure-ops-mcp && python -m venv .venv && source .venv/bin/activate
pip install -e . && make demo
```

## CI workflow (install once)

Template: [`docs/ci/demo.yml`](./ci/demo.yml). Copy to `.github/workflows/demo.yml` when your token has the `workflow` scope.
