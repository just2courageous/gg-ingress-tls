from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User

from diagrams.aws.network import Route53, ALB
from diagrams.aws.security import ACM
from diagrams.aws.compute import EKS

from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ingress, Service

graph_attr = {
    "pad": "1.0",
    "splines": "ortho",
    "nodesep": "1.1",
    "ranksep": "1.4",
    "fontsize": "12",
    "dpi": "300",
}

with Diagram(
    "GG Ingress TLS: Route53 + ExternalDNS + ALB Ingress + ACM on EKS",
    show=False,
    filename="docs/diagrams/gg-ingress-tls-arch",
    outformat="png",
    direction="LR",
    graph_attr=graph_attr,
):
    browser = User("User Browser\nhttps://app.<domain>")

    r53 = Route53("Route 53\nHosted Zone")

    with Cluster("AWS"):
        cert = ACM("ACM\nTLS Cert")
        alb = ALB("ALB\n(80/443)")
        eks = EKS("EKS\nCluster")

        with Cluster("Kubernetes"):
            ing = Ingress("Ingress\n(ALB annotations)")
            svc = Service("Service\nClusterIP")
            pods = Pod("Pods\nnginx demo")

    browser >> Edge(label="DNS lookup") >> r53
    r53 >> Edge(label="A/ALIAS → ALB") >> alb
    cert >> Edge(label="TLS") >> alb
    alb >> Edge(label="forwards") >> ing >> svc >> pods
    eks >> Edge(label="runs") >> pods
