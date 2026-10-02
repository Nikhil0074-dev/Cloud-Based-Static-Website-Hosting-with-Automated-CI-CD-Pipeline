variable "aws_region" {
  description = "Region for the S3 bucket."
  type        = string
  default     = "ap-south-1"
}

variable "bucket_name" {
  description = "Globally unique name for the website bucket."
  type        = string
}

variable "domain_name" {
  description = "Custom domain (for example www.example.com). Leave empty to use the default CloudFront domain."
  type        = string
  default     = ""
}

variable "route53_zone_name" {
  description = "Existing Route 53 hosted zone name (for example example.com). Required when domain_name is set."
  type        = string
  default     = ""
}

variable "github_repo" {
  description = "GitHub repository allowed to deploy, as owner/name."
  type        = string
}

variable "create_github_oidc_provider" {
  description = "Create the GitHub OIDC provider. Set to false if your AWS account already has one."
  type        = bool
  default     = true
}

variable "alert_email" {
  description = "Email address for 5xx error alarm notifications. Leave empty to skip."
  type        = string
  default     = ""
}
