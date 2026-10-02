#!/usr/bin/env bash
# Build the deployable site into ./dist and stamp it with version metadata.
set -euo pipefail
cd "$(dirname "$0")/.."

ENVIRONMENT="${ENVIRONMENT:-production}"
COMMIT="${GITHUB_SHA:-$(git rev-parse HEAD 2>/dev/null || echo unknown)}"
VERSION="${VERSION:-$(git describe --tags --always 2>/dev/null || echo "0.0.0-${COMMIT:0:7}")}"
BUILT_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

rm -rf dist
mkdir -p dist
cp -R website/. dist/

cat > dist/version.json <<JSON
{
  "status": "Deployed",
  "version": "${VERSION}",
  "commit": "${COMMIT:0:7}",
  "environment": "${ENVIRONMENT}",
  "built_at": "${BUILT_AT}",
  "history": [
    { "version": "${VERSION}", "commit": "${COMMIT:0:7}", "status": "Deployed", "date": "${BUILT_AT}" }
  ]
}
JSON

echo "Built dist/ (version ${VERSION}, commit ${COMMIT:0:7})"
