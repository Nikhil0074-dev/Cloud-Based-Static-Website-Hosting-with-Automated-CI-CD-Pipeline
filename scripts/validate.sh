#!/usr/bin/env bash
# Validate the project: required files, shell syntax, and the test suite.
set -euo pipefail
cd "$(dirname "$0")/.."

required=(website/index.html website/about.html website/projects.html website/contact.html
          website/404.html website/css/style.css website/js/main.js)
for f in "${required[@]}"; do
  [[ -f "$f" ]] || { echo "Missing required file: $f" >&2; exit 1; }
done

for s in scripts/*.sh; do bash -n "$s"; done
echo "Shell syntax OK"

python3 -m unittest discover -s tests -v
echo "Validation passed"
