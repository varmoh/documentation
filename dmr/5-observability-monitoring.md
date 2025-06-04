## Observability & Monitoring

This section focuses on giving visibility into how messages are flowing, where problems might be happening, and whether everything is healthy — without exposing sensitive data.

### Integrate RabbitMQ Metrics and Logs (Prometheus, Grafana)

RabbitMQ can export performance and usage metrics. These are collected using Prometheus and visualized in tools like Grafana. You’ll see metrics like queue lengths, message rates, connection counts, and failure spikes — helping operators understand system behavior in real time.

### Emit Structured Logs (e.g. Sender → Recipient, Result)

Each message transaction should generate a log entry in a structured JSON format. It includes who sent the message, who it was for, and whether it succeeded or failed (and why). These logs help with auditing, debugging, and alerting — and can be collected centrally (e.g., in ELK, Loki, or CentOps).

### Visualize Topology and Message Hops (Optional Traces)

If enabled, you can trace the full path a message took across DMR nodes. This includes IDs of each node it passed through and how long each hop took. This is useful for debugging complex routing issues or seeing latency patterns. This feature is optional and can be scoped per tenant/debug session.

### Log Configuration Reloads, Failed Deliveries, and Policy Violations

Any time a DMR reloads config (like a new cert, route, or policy), that event should be logged. If it fails, it should trigger an alert. Similarly, if a message fails delivery or breaks a security rule (like a bad cert or denied sender), that should also be logged and potentially trigger alerts.

### In Short

This section ensures you always know what’s happening inside the DMR mesh — what messages are doing, whether things are healthy, and where to look when something breaks — all without exposing private message content.
