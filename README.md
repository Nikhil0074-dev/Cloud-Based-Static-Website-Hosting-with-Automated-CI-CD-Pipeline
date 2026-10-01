# Cloud-Based Static Website Hosting with Automated CI/CD Pipeline

A portfolio website hosted on AWS (S3 + CloudFront + ACM + Route 53) and deployed
automatically by GitHub Actions. Infrastructure is defined with Terraform.

```
Developer -> GitHub -> GitHub Actions (validate, test, build, deploy)
          -> S3 (private origin) -> CloudFront (HTTPS) -> Users
          Route 53 + ACM for the domain, CloudWatch for monitoring
```

## Repository layout

| Path | Purpose |
|------|---------|
| `website/` | Static site (HTML, CSS, JS, SVG images, dashboard page) |
| `tests/` | Python `unittest` checks: HTML structure, links, assets, navigation, JS syntax |
| `scripts/` | `validate.sh`, `build.sh`, `deploy.sh` |
| `.github/workflows/` | `ci.yml` (pull requests), `deploy.yml` (main), `rollback.yml` (manual) |
| `terraform/` | S3, CloudFront, OAC, ACM, Route 53, IAM (OIDC), CloudWatch |
| `docs/` | Architecture, deployment, security, troubleshooting |

## Run locally

Requirements: Python 3.9+ and Bash. Node.js is optional (enables JavaScript syntax checks).

```bash
bash scripts/validate.sh        # runs all checks and tests
bash scripts/build.sh           # creates dist/ with version.json
python3 -m http.server -d website 8000   # preview at http://localhost:8000
```

## Deploy to AWS

1. Install Terraform (1.5+) and configure AWS credentials.
2. `cd terraform && cp terraform.tfvars.example terraform.tfvars`, then edit the values.
3. `terraform init && terraform apply`
4. In GitHub, go to Settings > Environments and create an environment named `production`
   (add required reviewers for manual approval).
5. In Settings > Secrets and variables > Actions > Variables, add these repository variables
   using the Terraform outputs: `AWS_ROLE_ARN`, `AWS_REGION`, `BUCKET_NAME`, `CLOUDFRONT_DISTRIBUTION_ID`.
6. Push to `main`. The Deploy workflow validates, builds, uploads to S3 and invalidates CloudFront.

See `docs/deployment.md` for details.

## Notes

- Edit the name, text and contact address (`hello@example.com` in `website/js/main.js`) to make the site your own.
- No long-lived AWS keys are used. GitHub authenticates to AWS with short-lived OIDC credentials.
