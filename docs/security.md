# Security

- **Least privilege:** the deploy role can list the bucket, get/put/delete objects in it, and create invalidations for this one distribution.
- **OIDC:** the role trusts only `repo:<owner>/<repo>:environment:production`, so only jobs in that environment can deploy. No AWS keys are stored in GitHub.
- **Private origin:** S3 blocks all public access. Only this CloudFront distribution can read objects, through Origin Access Control.
- **HTTPS:** HTTP redirects to HTTPS. Custom domains use TLS 1.2 or newer. The managed security headers policy is applied.
- **Encryption and versioning:** S3 encrypts objects at rest and keeps previous versions.
- **Scanning:** CI runs Trivy for vulnerabilities, secrets and misconfigurations.
- **Recommended GitHub settings:** protect `main`, require pull requests, require the CI checks, and require reviewers on the `production` environment.
