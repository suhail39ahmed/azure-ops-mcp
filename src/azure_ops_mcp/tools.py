"""Fixture-backed Azure ops tools. Dry-run by default. No live Azure calls."""
from __future__ import annotations

import json
from pathlib import Path


def kv_compare(left: Path, right: Path) -> dict:
    a = json.loads(left.read_text(encoding="utf-8"))
    b = json.loads(right.read_text(encoding="utf-8"))
    keys = sorted(set(a) | set(b))
    diffs = []
    for k in keys:
        if a.get(k) != b.get(k):
            diffs.append({"key": k, "left": a.get(k), "right": b.get(k)})
    return {
        "ok": True,
        "action": "kv_compare",
        "left": str(left),
        "right": str(right),
        "diff_keys": [d["key"] for d in diffs],
        "diffs": diffs,
        "notes": [
            "Never echo secret *values* — fixtures list secret names only.",
            "Prod should enable purge protection and Deny network default.",
        ],
    }


def ado_diagnose(fixture: Path) -> dict:
    data = json.loads(fixture.read_text(encoding="utf-8"))
    msg = (data.get("message") or "").lower()
    remediation = "Inspect failing task and recent changes."
    if "aadsts7000222" in msg or "expired" in msg:
        remediation = "Rotate service connection secret or move to workload identity federation. Human approval required."
    return {
        "ok": True,
        "action": "ado_diagnose",
        "pipeline": data.get("pipeline"),
        "runId": data.get("runId"),
        "failingTask": data.get("failingTask"),
        "summary": data.get("message"),
        "remediation": remediation,
        "human_approval_required": True,
    }


def cost_stub(fixture: Path, top_n: int = 3) -> dict:
    data = json.loads(fixture.read_text(encoding="utf-8"))
    items = sorted(data.get("items") or [], key=lambda x: x.get("cost", 0), reverse=True)
    total = sum(i.get("cost", 0) for i in items)
    return {
        "ok": True,
        "action": "cost_stub",
        "subscription": data.get("subscription"),
        "currency": data.get("currency", "USD"),
        "total": total,
        "top": items[:top_n],
        "disclaimer": "Stub data only — not a live Cost Management query.",
    }
