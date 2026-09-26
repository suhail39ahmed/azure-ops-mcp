from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def audit(log_path: Path, tool: str, args: dict, result: dict, dry_run: bool) -> None:
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "tool": tool,
        "dry_run": dry_run,
        "args": args,
        "result_summary": {k: result.get(k) for k in ("ok", "action", "diff_keys", "total") if k in result},
    }
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
