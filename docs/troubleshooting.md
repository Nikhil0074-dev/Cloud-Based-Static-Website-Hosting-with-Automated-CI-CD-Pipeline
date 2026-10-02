# Troubleshooting

| Problem | Fix |
|---------|-----|
| `Not authorized to perform sts:AssumeRoleWithWebIdentity` | The job must use `environment: production`, and `github_repo` in Terraform must match `owner/name` exactly. |
| `EntityAlreadyExists` for the OIDC provider | Set `create_github_oidc_provider = false` and apply again. |
| Site shows old content | HTML is uploaded with `no-cache` and CloudFront is invalidated on deploy. Check that the Deploy run finished. |
| Every page returns 404 | The bucket is empty. Run the Deploy workflow or `scripts/deploy.sh`. |
| Certificate stays pending | The Route 53 zone must be the public zone for the domain, and nameservers must point to it. |
| Bucket name error | S3 bucket names are global. Choose another `bucket_name`. |
| `validate.sh` fails locally | Read the failing test name. Tests report the page and the broken link or tag. |
