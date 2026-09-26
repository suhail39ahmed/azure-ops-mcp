"""Optional MCP stdio server (requires: pip install -e '.[mcp]')."""
from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError:
        print(
            "mcp package not installed. Run: pip install -e '.[mcp]'\n"
            "Or use the CLI: python -m azure_ops_mcp --help",
            file=sys.stderr,
        )
        raise SystemExit(1) from None

    from .tools import ado_diagnose, cost_stub, kv_compare

    mcp = FastMCP("azure-ops-mcp")

    @mcp.tool()
    def kv_compare_tool(left: str, right: str) -> dict:
        """Compare two Key Vault config fixtures (dry-run / offline)."""
        return kv_compare(Path(left), Path(right))

    @mcp.tool()
    def ado_diagnose_tool(fixture: str) -> dict:
        """Diagnose an ADO failed-job fixture (offline)."""
        return ado_diagnose(Path(fixture))

    @mcp.tool()
    def cost_stub_tool(fixture: str, top: int = 3) -> dict:
        """Stub cost rollup from a fixture JSON file."""
        return cost_stub(Path(fixture), top)

    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
