# gg-ingress-tls

**Goal:** Expose an app on **EKS** via **ALB Ingress**, with **DNS** managed in **Route 53 (AWS managed DNS (Domain Name System))** using **ExternalDNS**, and **TLS (Transport Layer Security)** via **ACM (AWS Certificate Manager)**.

## Architecture diagram
![GG Ingress TLS architecture](docs/diagrams/gg-ingress-tls-arch.png)

Editable source:
- docs/diagrams/gg-ingress-tls-arch.drawio

## Environment
- **AWS (Amazon Web Services) Account:** 399717050894
- **Region:** us-east-2
- **Cluster:** green-guard-gg-eks
- **Host:** app.courageerhabor.com (delegated subdomain)

## Repo structure
- `infra/` — **eksctl** parity config/pointer (this repo does **not** store Terraform (Infrastructure as Code) for EKS (Elastic Kubernetes Service))
- `k8s/` — Kubernetes manifests
- `scripts/` — Bash helpers
- `docs/screenshots/` — proofs
- `docs/diagrams/` — diagrams
- `.github/` — CI config (if present)

## Proofs (screenshots)
- docs/screenshots/06-eksctl-create-finished.png
- docs/screenshots/08-alb-controller-active.png
- docs/screenshots/09-externaldns-installed.png
- docs/screenshots/10-r53-subzone-created.png
- docs/screenshots/12-namecheap-ns-delegation.png
- docs/screenshots/16-acm-issued.png
- docs/screenshots/20-browser-https.png
- docs/screenshots/22-alb-listeners.png
- docs/screenshots/23-targets-healthy.png

## Cleanup
- Delete the Ingress (Kubernetes Ingress) to remove the ALB.
- Optionally delete the EKS cluster to stop costs.
