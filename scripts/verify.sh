#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
case "${1:-}" in
    --integrity-only) [[ $# -eq 1 ]] || exit 2 ;;
    "") [[ $# -eq 0 ]] || exit 2 ;;
    *) echo 'Usage: bash scripts/verify.sh [--integrity-only]' >&2; exit 2 ;;
esac
python3 -B scripts/verify_tree.py
python3 -B scripts/check_paper.py paper/manuscript.pdf
if [[ $# -eq 0 ]]; then
    python3 -B verification/run.py --max-order 9
fi
