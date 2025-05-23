```mermaid
graph TD
  A[Telemetry]
  A --> B[Uptime by Environment]
  A --> C[Error Rate Over Time]
  A --> D[Response Time]
  B --> E[Prometheus /metrics Endpoint]
  C --> E
  D --> E
  A --> F[Grafana Dashboards Integratsioon]
