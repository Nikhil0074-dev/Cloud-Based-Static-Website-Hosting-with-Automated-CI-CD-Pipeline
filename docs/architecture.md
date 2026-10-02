# Architecture

1. A developer pushes a branch and opens a pull request.
2. `ci.yml` validates HTML/CSS/JS, runs the tests, scans for vulnerabilities, secrets and misconfigurations, and validates Terraform.
3. After review, the merge to `main` triggers `deploy.yml`. It tests again, builds `dist/`, assumes an AWS role through OIDC, syncs files to S3 and invalidates CloudFront.
4. S3 is private. CloudFront reads it through Origin Access Control and serves the site over HTTPS. Missing files return `404.html`.
5. With a custom domain, ACM issues the certificate (DNS validation) and Route 53 aliases the domain to CloudFront.
6. CloudWatch shows requests, error rates, cache hit rate and origin latency, and alarms on a high 5xx rate.

Environments: the `production` GitHub environment gates deployment. To add staging, copy the Terraform with a different `bucket_name` and add a workflow that deploys the `develop` branch to it.
