#!/usr/bin/env bash
# Upload ./dist to S3 and invalidate CloudFront.
# Required env: BUCKET_NAME, CLOUDFRONT_DISTRIBUTION_ID (AWS credentials come from the environment).
set -euo pipefail
cd "$(dirname "$0")/.."

: "${BUCKET_NAME:?Set BUCKET_NAME}"
: "${CLOUDFRONT_DISTRIBUTION_ID:?Set CLOUDFRONT_DISTRIBUTION_ID}"
[[ -d dist ]] || { echo "dist/ not found. Run scripts/build.sh first." >&2; exit 1; }

# Static assets: cache for a day.
aws s3 sync dist "s3://${BUCKET_NAME}" --delete \
  --exclude "*.html" --exclude "version.json" \
  --cache-control "public,max-age=86400"

# HTML and version metadata: always revalidate.
aws s3 sync dist "s3://${BUCKET_NAME}" --delete \
  --exclude "*" --include "*.html" --include "version.json" \
  --cache-control "no-cache"

aws cloudfront create-invalidation \
  --distribution-id "${CLOUDFRONT_DISTRIBUTION_ID}" --paths "/*"

echo "Deployment complete"
