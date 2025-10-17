# gg-ingress-tls
**Goal:** Expose an app on **EKS (Elastic Kubernetes Service)** via **ALB (Application Load Balancer) Ingress** with **DNS (Domain Name System)** managed in **Route 53 (AWS Managed DNS)** using **ExternalDNS (External Domain Name System)**, and **TLS (Transport Layer Security)** via **ACM (AWS Certificate Manager)**.
## Environment
- **AWS (Amazon Web Services) Account:** 399717050894
- **Region:** us-east-2
- **Cluster:** green-guard-gg-eks
- **Host:** app.courageerhabor.com (delegated subdomain)
## Structure
- `infra/` — Terraform (Infrastructure as Code)
- `k8s/` — Kubernetes manifests
- `scripts/` — Bash (Bourne Again SHell) helpers
- `docs/screenshots/` — proofs
- `docs/diagrams/` — diagrams
- `.github/workflows/` — CI (Continuous Integration)
## Proofs (screenshots)
- alb-controller-active.png
- r53-subzone-created.png
- r53-subzone-ns.png
- 43-acm-requested.png
- 43-acm-issued.png
- ingress-created.png
- r53-alias.png
- browser-https.png
- alb-target-healthy.png
## Cleanup
- Delete Ingress → removes ALB (Application Load Balancer).
- Optionally destroy the cluster to stop costs.
