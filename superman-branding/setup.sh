#!/usr/bin/env bash
# Creates a fully customized checkout of InvisiProxy LTS, rather than a second proxy engine.
set -Eeuo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="${1:-$HERE/SUPERMAN-BROWSER}"
if ! command -v git >/dev/null; then echo 'Git is required.'; exit 1; fi
if ! command -v python3 >/dev/null; then echo 'Python 3 is required.'; exit 1; fi
if [ ! -d "$TARGET/.git" ]; then
  echo 'Cloning the official current InvisiProxyLTS master source...'
  git clone --recurse-submodules https://github.com/InvisiProxy/InvisiProxyLTS.git "$TARGET"
fi
python3 "$HERE/brand_superman.py" "$TARGET"
echo 'SUPERMAN source ready:' "$TARGET"
echo 'Next: cd' "$TARGET"
echo 'Then follow upstream Node 26/pnpm installation: pnpm run fresh-install && pnpm start'
