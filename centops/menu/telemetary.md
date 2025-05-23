```mermaid
graph TD
  A[Telemetry]
  A --> B[Uptime by Environment]
  A --> C[Error Rate Over Time]
  B --> E[Prometheus /metrics Endpoint]
  C --> E

  A --> F[Grafana Dashboards Integratsioon]
