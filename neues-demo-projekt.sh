#!/usr/bin/env bash
# Legt ein frisches Demo-Projekt aus der Vorlage an (Standard: ../quadratic-demo).
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
ZIEL="${1:-$HERE/../quadratic-demo}"

if [ -e "$ZIEL" ]; then
    echo "Ziel existiert bereits: $ZIEL" >&2
    echo "Zum Zurücksetzen erst löschen: rm -rf \"$ZIEL\"" >&2
    exit 1
fi

cp -r "$HERE/vorlage" "$ZIEL"
cd "$ZIEL"
git init -q -b main
git add -A
git commit -q -m "Gerüst aus Vorlage"
echo "Demo-Projekt angelegt: $(pwd)"
echo "Weiter: python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements-dev.txt"
