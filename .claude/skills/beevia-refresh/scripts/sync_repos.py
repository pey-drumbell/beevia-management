#!/usr/bin/env python3
"""Fast-forward every Beevia sub-repo to origin/main and report what changed.

This is the ONE place in the workspace tooling that writes to the service
repositories, and it is deliberately limited to git-level synchronisation:
checkout, fetch, fast-forward. It never edits a file, never commits, never
pushes, and never resolves a conflict.

Safety rules, in priority order:

  1. A repo with uncommitted changes is SKIPPED ENTIRELY — not stashed.
     Stashing hides work behind a command the user did not run and did not see
     fail. Skipping is loud and reversible; stashing is quiet and easy to lose.
  2. Merges are `--ff-only`. A divergent local main stops with a report rather
     than producing a merge commit nobody asked for.
  3. The branch a repo was on is always reported, so switching away from a
     feature branch is visible rather than silent.

Usage:
    python3 sync_repos.py                 # sync all repos to main
    python3 sync_repos.py --dry-run       # report what would happen
    python3 sync_repos.py --no-switch     # pull current branch, do not checkout main
    python3 sync_repos.py --json          # machine-readable, for the audit step
    python3 sync_repos.py --repo beevia-api --repo beevia-admin-api

Exit codes:
    0  every repo is clean and up to date
    1  at least one repo was skipped, diverged, or failed to sync
    2  could not run at all (not a workspace, git missing)
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys

# Order matters only for readability of the report.
REPOS = [
    "beevia-api",
    "beevia-admin-api",
    "beevia-db-schema",
    "beevia-admin",
    "beevia-mobile",
]

# Paths whose changes should pull the reviewer's eye. A commit touching only a
# README does not need an OpenAPI re-read; one touching a controller does.
INTERESTING = (
    ".controller.ts", ".dto.ts", "/dto/", ".guard.ts", ".module.ts",
    "/schema/", "enums.ts", "main.ts", ".service.ts",
)


def run(args: list[str], cwd: str) -> tuple[int, str]:
    """Run a git command, returning (exit_code, combined_output)."""
    try:
        p = subprocess.run(args, cwd=cwd, capture_output=True, text=True,
                           timeout=180)
    except subprocess.TimeoutExpired:
        return 124, "timed out"
    except FileNotFoundError:
        return 127, "git not found"
    return p.returncode, (p.stdout + p.stderr).strip()


def git(cwd: str, *args: str) -> str:
    """Run git and return stdout, or "" on failure."""
    code, out = run(["git", *args], cwd)
    return out if code == 0 else ""


def workspace_root() -> str:
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, ".claude")) and \
                os.path.basename(d) != ".claude":
            return d
        d = os.path.dirname(d)
    return os.getcwd()


ROOT = os.environ.get("BEEVIA_ROOT") or workspace_root()


def classify(files: list[str]) -> list[str]:
    """Files most likely to change the API surface, newest-first order kept."""
    return [f for f in files if any(m in f for m in INTERESTING)]


def sync_one(name: str, switch: bool, dry: bool) -> dict:
    """Sync a single repo. Returns a result record; never raises."""
    path = os.path.join(ROOT, name)
    r: dict = {"repo": name, "status": "ok", "branch_before": None,
               "branch_after": None, "pulled": 0, "commits": [],
               "changed_files": [], "api_files": [], "note": ""}

    if not os.path.isdir(os.path.join(path, ".git")):
        r["status"] = "missing"
        r["note"] = "not a git repository"
        return r

    branch = git(path, "rev-parse", "--abbrev-ref", "HEAD")
    r["branch_before"] = r["branch_after"] = branch or "(detached)"

    # Uncommitted work is a hard stop. Checking out or pulling over it either
    # fails noisily or silently carries changes onto another branch.
    dirty = git(path, "status", "--porcelain")
    if dirty:
        r["status"] = "skipped-dirty"
        r["note"] = (f"{len(dirty.splitlines())} uncommitted change(s) — "
                     f"not touched. Commit or stash, then re-run.")
        return r

    code, out = run(["git", "fetch", "origin", "--prune"], path)
    if code != 0:
        r["status"] = "fetch-failed"
        r["note"] = out.splitlines()[-1] if out else "fetch failed"
        return r

    if not git(path, "rev-parse", "--verify", "origin/main"):
        r["status"] = "no-main"
        r["note"] = "origin/main does not exist"
        return r

    before = git(path, "rev-parse", "HEAD")

    if switch and branch != "main":
        if dry:
            r["note"] = f"would switch {branch} -> main"
        else:
            code, out = run(["git", "checkout", "main"], path)
            if code != 0:
                r["status"] = "checkout-failed"
                r["note"] = out.splitlines()[-1] if out else "checkout failed"
                return r
        r["branch_after"] = "main"

    if dry:
        behind = git(path, "rev-list", "--count", "HEAD..origin/main") or "0"
        r["pulled"] = int(behind)
        r["note"] = (r["note"] + "; " if r["note"] else "") + \
                    f"would fast-forward {behind} commit(s)"
        return r

    # --ff-only: a divergent local branch should stop the run, not silently
    # produce a merge commit in a repo this tool is only meant to read.
    code, out = run(["git", "merge", "--ff-only", "origin/main"], path)
    if code != 0:
        r["status"] = "diverged"
        r["note"] = ("local main has commits not on origin/main — "
                     "fast-forward refused. Resolve by hand.")
        return r

    after = git(path, "rev-parse", "HEAD")
    if before and after and before != after:
        log = git(path, "log", "--oneline", "--no-decorate", f"{before}..{after}")
        r["commits"] = log.splitlines()
        r["pulled"] = len(r["commits"])
        files = git(path, "diff", "--name-only", before, after)
        r["changed_files"] = files.splitlines()
        r["api_files"] = classify(r["changed_files"])
    return r


def report(results: list[dict], dry: bool = False) -> None:
    print(f"Workspace: {ROOT}\n")
    width = max(len(r["repo"]) for r in results)
    for r in results:
        mark = {"ok": "  ", "skipped-dirty": "!!", "diverged": "!!",
                "fetch-failed": "!!", "checkout-failed": "!!",
                "no-main": "!!", "missing": "??"}.get(r["status"], "!!")
        branch = r["branch_before"]
        if r["branch_after"] != r["branch_before"]:
            branch = f"{r['branch_before']} -> {r['branch_after']}"
        line = f"{mark} {r['repo']:<{width}}  {branch:<26}"
        if r["status"] == "ok":
            line += f"+{r['pulled']} commit(s)" if r["pulled"] else "up to date"
        else:
            line += r["status"]
        print(line)
        if r["note"]:
            print(f"     {r['note']}")
        for c in r["commits"][:8]:
            print(f"       {c}")
        if len(r["commits"]) > 8:
            print(f"       … {len(r['commits']) - 8} more")
        if r["api_files"]:
            print(f"     API-relevant files ({len(r['api_files'])}):")
            for f in r["api_files"][:12]:
                print(f"       {f}")
            if len(r["api_files"]) > 12:
                print(f"       … {len(r['api_files']) - 12} more")

    changed = [r for r in results if r["pulled"]]
    blocked = [r for r in results if r["status"] not in ("ok", "missing")]
    print()
    if changed:
        total = sum(r["pulled"] for r in changed)
        verb = "Would pull" if dry else "Pulled"
        print(f"{verb} {total} commit(s) across {len(changed)} repo(s): "
              f"{', '.join(r['repo'] for r in changed)}")
        if dry:
            # The diff is only inspected on a real run, so saying anything
            # about which files moved would be a guess dressed as a finding.
            print("Run without --dry-run to see which files changed.")
        else:
            api = [r["repo"] for r in changed if r["api_files"]]
            if api:
                print(f"API surface may have moved in: {', '.join(api)} "
                      f"-> re-run the audit and check the specs.")
            else:
                print("No controller/DTO/schema files touched — "
                      "the OpenAPI specs are unlikely to need changes.")
    else:
        print("Everything already up to date.")
    if blocked:
        print(f"\n{len(blocked)} repo(s) NOT synced: "
              f"{', '.join(r['repo'] for r in blocked)}")
        print("The audit will run against stale code for those.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would happen, change nothing")
    ap.add_argument("--no-switch", action="store_true",
                    help="pull the current branch instead of checking out main")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--repo", action="append",
                    help="limit to one repo (repeatable)")
    args = ap.parse_args()

    if not os.path.isdir(os.path.join(ROOT, ".claude")):
        print(f"ERROR: {ROOT} is not the Beevia workspace", file=sys.stderr)
        return 2

    targets = args.repo or REPOS
    results = [sync_one(n, switch=not args.no_switch, dry=args.dry_run)
               for n in targets]

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        report(results, dry=args.dry_run)

    return 1 if any(r["status"] not in ("ok", "missing") for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
