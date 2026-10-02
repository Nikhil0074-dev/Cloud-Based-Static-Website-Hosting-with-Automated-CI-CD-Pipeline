# Deployment

## One-time setup
Follow the "Deploy to AWS" steps in the README. Terraform outputs give the values for the GitHub variables:
`terraform output bucket_name`, `cloudfront_distribution_id`, `deploy_role_arn`.

If your AWS account already has the GitHub OIDC provider, set `create_github_oidc_provider = false`.

## Custom domain
Set `domain_name` (for example `www.example.com`) and `route53_zone_name` (for example `example.com`) in `terraform.tfvars`. The hosted zone must already exist.

## Normal release
Open a pull request, wait for CI, get it reviewed, merge. Deploy runs automatically. If the `production` environment has required reviewers, approve the run in GitHub.

## Rollback
Run the **Rollback** workflow from the Actions tab and enter a tag, branch or commit SHA. It rebuilds that version and redeploys it. S3 versioning also keeps earlier copies of each file for 90 days.

## Manual deploy
```bash
export BUCKET_NAME=... CLOUDFRONT_DISTRIBUTION_ID=...
bash scripts/build.sh && bash scripts/deploy.sh
```
