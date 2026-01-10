# Infrastructure (P2 — Ingress/DNS/TLS)

This repo focuses on **Ingress (ALB)**, **ExternalDNS (Route 53)**, and **ACM/TLS** on top of an existing EKS cluster.

## How the cluster was created (parity)
We used **eksctl** (not Terraform) when building P2.

- Region: us-east-2
- OIDC enabled (IRSA)
- Managed node group: ng-main

## Where Terraform lives
Full EKS + VPC Terraform (IaC) is tracked in the main Green-Guard repo (separate from this P2 repo).
