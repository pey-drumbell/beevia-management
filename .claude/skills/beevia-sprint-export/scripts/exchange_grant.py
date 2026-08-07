#!/usr/bin/env python3
"""Exchange a Zoho Self Client grant token for a long-lived refresh token.

The Self Client tab hands you a GRANT token (an authorization code). It is
one-time and expires in ~10 minutes. It is NOT a refresh token, and pasting it
straight into ZOHO_REFRESH_TOKEN fails with {'error': 'invalid_code'} — which
reads like a bad token rather than a missed step.

Usage
-----
    # after pasting the grant code into ZOHO_REFRESH_TOKEN in .env:
    python3 exchange_grant.py

    # or pass it directly, leaving .env alone until the call succeeds:
    python3 exchange_grant.py --code 1000.abc....

On success the refresh token is written back to .env in place and the stale
access-token cache is removed. The token itself is never printed.

Exit codes: 0 written · 1 config/API error · 2 code expired or already used.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
ENV = os.path.join(ROOT, ".env")
CACHE = os.path.join(ROOT, ".zoho-token-cache.json")

REQUIRED_SCOPES = (
    "ZohoSprints.teams.READ",
    "ZohoSprints.projects.READ",
    "ZohoSprints.sprints.READ",
    "ZohoSprints.items.READ",
    "ZohoSprints.epic.READ",
)


def read_env(path: str) -> dict[str, str]:
    env: dict[str, str] = {}
    with open(path) as fh:
        for line in fh:
            s = line.strip()
            if s and not s.startswith("#") and "=" in s:
                k, v = s.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--code", help="grant token; defaults to ZOHO_REFRESH_TOKEN in .env")
    ap.add_argument("--dry-run", action="store_true", help="exchange but do not write .env")
    args = ap.parse_args()

    if not os.path.exists(ENV):
        print(f"ERROR: no .env at {ENV}", file=sys.stderr)
        return 1

    env = read_env(ENV)
    missing = [k for k in ("ZOHO_CLIENT_ID", "ZOHO_CLIENT_SECRET") if not env.get(k)]
    if missing:
        print(f"ERROR: .env is missing {', '.join(missing)}", file=sys.stderr)
        return 1

    # ZOHO_CLIENT_GRANT_CODE is the correct home for the one-time code.
    # ZOHO_REFRESH_TOKEN is accepted as a fallback only because pasting the
    # grant code there is the mistake this script exists to recover from.
    code = (args.code
            or env.get("ZOHO_CLIENT_GRANT_CODE", "")
            or env.get("ZOHO_REFRESH_TOKEN", ""))
    if not code:
        print("ERROR: no grant code. Pass --code or set ZOHO_CLIENT_GRANT_CODE.",
              file=sys.stderr)
        return 1

    dc = env.get("ZOHO_DC", "com")
    url = f"https://accounts.zoho.{dc}/oauth/v2/token"
    body = urllib.parse.urlencode({
        "grant_type": "authorization_code",
        "client_id": env["ZOHO_CLIENT_ID"],
        "client_secret": env["ZOHO_CLIENT_SECRET"],
        "code": code,
    }).encode()

    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=body)) as resp:
            res = json.load(resp)
    except urllib.error.HTTPError as exc:
        print(f"ERROR: HTTP {exc.code} from {url}", file=sys.stderr)
        return 1
    except Exception as exc:  # noqa: BLE001 - network shape varies
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if "refresh_token" not in res:
        err = res.get("error", "<none>")
        print(f"EXCHANGE FAILED: {err}", file=sys.stderr)
        if err == "invalid_code":
            print(
                "\n  A grant token is one-time and lives ~10 minutes. This one is\n"
                "  expired or already used. Generate a fresh one in the Self Client\n"
                "  tab and run this again straight away.\n"
                "  Scopes to request:\n    " + ",".join(REQUIRED_SCOPES),
                file=sys.stderr,
            )
            return 2
        return 1

    scope = res.get("scope", "")
    print("EXCHANGE OK")
    print(f"  granted scope : {scope or '<not returned>'}")

    granted = set(scope.split()) | set(scope.split(","))
    absent = [s for s in REQUIRED_SCOPES if s not in granted]
    if scope and absent:
        print(f"  WARNING       : missing {', '.join(absent)}")
        print("                  the export will run but those columns stay blank")
    elif scope:
        print("  all five required scopes present")

    if args.dry_run:
        print("  --dry-run: .env not written")
        return 0

    src = open(ENV).read()
    line = "ZOHO_REFRESH_TOKEN=" + res["refresh_token"]
    new, n = re.subn(r"(?m)^ZOHO_REFRESH_TOKEN=.*$", line, src)
    if n == 0:
        # The variable may legitimately be absent — first-time setup, or the
        # user removed it. Append rather than fail.
        if not new.endswith("\n"):
            new += "\n"
        new += line + "\n"
        print("  .env updated  : ZOHO_REFRESH_TOKEN appended (value not printed)")
    elif n == 1:
        print("  .env updated  : ZOHO_REFRESH_TOKEN replaced (value not printed)")
    else:
        print(f"ERROR: found {n} ZOHO_REFRESH_TOKEN lines; refusing to write.",
              file=sys.stderr)
        return 1

    # A spent grant code is useless and only invites confusion next time.
    new = re.sub(r"(?m)^ZOHO_CLIENT_GRANT_CODE=.*$",
                 "ZOHO_CLIENT_GRANT_CODE=   # spent — regenerate in the Self Client tab",
                 new)

    with open(ENV, "w") as fh:
        fh.write(new)
    os.chmod(ENV, 0o600)
    if os.path.exists(CACHE):
        os.remove(CACHE)
        print("  cache cleared : .zoho-token-cache.json removed")

    return 0


if __name__ == "__main__":
    sys.exit(main())
