#!/usr/bin/env bash
# Local build of the site with the k11h theme into output/ and serve it.
# usage: themes/serve.sh [port]     needs pelican[markdown] (or PELICAN=/path/to/pelican)
set -euo pipefail
cd "$(dirname "$0")/.."
PELICAN=${PELICAN:-pelican}
"$PELICAN" content -s pelicanconf.py -o output -lr -p "${1:-8000}"
