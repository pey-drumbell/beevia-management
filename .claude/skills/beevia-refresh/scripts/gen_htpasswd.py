#!/usr/bin/env python3
"""Generate web-report/.htpasswd from WEB_REPORTS_USER / WEB_REPORTS_PASSWORD
in .env, for the Basic-Auth privacy gate on the shared-hosting deploy.

Not hardened security — a lightweight login so the reports aren't fully
public. Rerun this any time the username or password in .env changes; it
overwrites web-report/.htpasswd in place.

Uses `openssl passwd -apr1`, the exact hash format Apache's own `htpasswd -m`
produces, so it needs no htpasswd binary. The password is piped to openssl
via stdin and is never written to argv, a log, or stdout — only the
resulting hash (safe to print) and the username appear in this script's
output.

Usage:
    python3 gen_htpasswd.py
"""
from __future__ import annotations

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
ENV = os.path.join(ROOT, ".env")
OUT = os.path.join(ROOT, "web-report", ".htpasswd")


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
    if not os.path.exists(ENV):
        print(f"ERROR: no .env at {ENV}", file=sys.stderr)
        return 1

    env = read_env(ENV)
    password = env.get("WEB_REPORTS_PASSWORD")
    username = env.get("WEB_REPORTS_USER", "beevia")
    if not password:
        print("ERROR: WEB_REPORTS_PASSWORD not set in .env", file=sys.stderr)
        return 1

    result = subprocess.run(
        ["openssl", "passwd", "-apr1", "-stdin"],
        input=password.encode(), capture_output=True,
    )
    if result.returncode != 0:
        print("ERROR: openssl failed: " + result.stderr.decode(), file=sys.stderr)
        return 1

    digest = result.stdout.decode().strip()
    with open(OUT, "w") as fh:
        fh.write(f"{username}:{digest}\n")
    # 644, not 600: on shared hosting the Apache worker almost never runs as
    # the SSH/deploy account, so a stricter mode leaves mod_authn_file unable
    # to open the file at all — Apache then fails with 500 before it ever
    # reaches the password check, which reads exactly like a bad password
    # but isn't one. deploy_staging.sh's `rsync -a` preserves this mode on
    # every deploy, so getting it right here is what keeps it right on the
    # server. Safe regardless: .htaccess's <FilesMatch "^\.ht"> blocks any
    # direct HTTP request to this file irrespective of filesystem mode.
    os.chmod(OUT, 0o644)

    print(f"Wrote {OUT}")
    print(f"  username: {username}")
    print(f"  digest  : {digest}")
    print()
    print("Upload web-report/.htpasswd alongside .htaccess. The .htaccess")
    print("AuthUserFile line still needs the real absolute path on the host —")
    print("see the comment block at the top of web-report/.htaccess.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
