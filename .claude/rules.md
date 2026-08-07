The root folder is to manage the Beevia project, which consists of individual repos for each component, located in sub-folders.
Do not make any changes whatsoever to any of the following sub-folders unless specifically asked to:
beevia-admin
beevia-admin-api
beevia-api
beevia-db-schema
beevia-mobile

## Standing exception: repo synchronisation

The `beevia-refresh` skill is permitted to run **git synchronisation only** in
those sub-folders: `fetch`, `checkout main`, and `merge --ff-only origin/main`,
via `.claude/skills/beevia-refresh/scripts/sync_repos.py`.

That is the entire exception. Even under it, nothing may edit a file, commit,
push, force anything, or resolve a conflict in a sub-repo. A repo with
uncommitted changes is skipped rather than stashed, and a diverged branch stops
with a report rather than being merged.

Analysis output — OpenAPI specs, RFCs, status reports — is always written at the
workspace root or in `project-status/`, never inside a sub-repo.