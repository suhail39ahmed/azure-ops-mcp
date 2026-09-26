from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from .audit import audit
from .tools import ado_diagnose, cost_stub, kv_compare


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="azure-ops-mcp", description="Azure ops tools (fixture / dry-run)")
    p.add_argument("--dry-run", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--audit-log", type=Path, default=Path(os.environ.get("AZURE_OPS_AUDIT_LOG", "audit.log")))
    sub = p.add_subparsers(dest="cmd", required=True)

    k = sub.add_parser("kv-compare")
    k.add_argument("left", type=Path)
    k.add_argument("right", type=Path)

    a = sub.add_parser("ado-diagnose")
    a.add_argument("fixture", type=Path)

    c = sub.add_parser("cost-stub")
    c.add_argument("fixture", type=Path)
    c.add_argument("--top", type=int, default=3)

    args = p.parse_args(argv)
    if args.cmd == "kv-compare":
        result = kv_compare(args.left, args.right)
        tool_args = {"left": str(args.left), "right": str(args.right)}
        tool = "kv_compare"
    elif args.cmd == "ado-diagnose":
        result = ado_diagnose(args.fixture)
        tool_args = {"fixture": str(args.fixture)}
        tool = "ado_diagnose"
    else:
        result = cost_stub(args.fixture, args.top)
        tool_args = {"fixture": str(args.fixture), "top": args.top}
        tool = "cost_stub"

    result["dry_run"] = args.dry_run
    audit(args.audit_log, tool, tool_args, result, args.dry_run)
    print(json.dumps(result, indent=2))
    print(f"# audited -> {args.audit_log}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
