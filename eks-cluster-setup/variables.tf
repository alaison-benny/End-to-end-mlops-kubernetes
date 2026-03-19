variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "sentiments-eks"
}

variable "cluster_version" {
  description = "EKS cluster version"
  type        = string
  default     = "1.29"
}

