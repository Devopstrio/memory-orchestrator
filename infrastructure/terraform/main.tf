terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-west-2"
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = "memory-orchestrator-cluster"
  cluster_version = "1.30"
  vpc_id          = "vpc-87654321"
  subnet_ids      = ["subnet-012abcde", "subnet-12abcde0"]
}
