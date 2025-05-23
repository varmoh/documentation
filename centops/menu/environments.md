```mermaid
graph TD
  A[Environments]
  A --> B[Klientide Keskkondade Nimekiri]
  A --> C[Komponentide Info]
  A --> F[Secrets - kliendipõhised]
A --> D
  D[Telemetry]
  D --> G[Uptime by Environment]
  G --> H[Error Rate Over Time]
  H --> I[Prometheus /metrics Endpoint]
  I --> J

  J --> K[Grafana Dashboards Integratsioon]
