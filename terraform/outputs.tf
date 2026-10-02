output "bucket_name" {
  description = "Set as the BUCKET_NAME variable in GitHub."
  value       = aws_s3_bucket.site.bucket
}

output "cloudfront_distribution_id" {
  description = "Set as the CLOUDFRONT_DISTRIBUTION_ID variable in GitHub."
  value       = aws_cloudfront_distribution.site.id
}

output "deploy_role_arn" {
  description = "Set as the AWS_ROLE_ARN variable in GitHub."
  value       = aws_iam_role.deploy.arn
}

output "website_url" {
  description = "Public URL of the website."
  value       = local.use_domain ? "https://${var.domain_name}" : "https://${aws_cloudfront_distribution.site.domain_name}"
}
