## Operational Resilience

This section focuses on ensuring that the DMR system can recover from failures — like crashes, certificate problems, or network issues — without manual intervention or permanent outages.

### DMR Self-Healing on Cert Loss or Restart

If a DMR node loses its certificate (e.g., due to expiry or file corruption) or restarts, it should be able to automatically request a new certificate (e.g., from CentOps), reload it, and resume operation — without needing a human to fix it.

### Graceful Recovery of RabbitMQ Clients

If a client temporarily disconnects from the message system (e.g., due to a reboot or network issue), RabbitMQ should handle the reconnection and resume message flow without message loss or duplicate deliveries. This includes setting proper TTLs, queues, and reconnection logic.

### Network Partition Handling

If part of the DMR network becomes unreachable (a partition), the system should detect this and:

- **Retry connections**
- **Avoid message corruption or duplication**
- **Resume routing once the partition is resolved**

This is key to running in real-world distributed environments with intermittent connectivity.

### Config Validation Before Applying

When new configurations (like routing rules, policies, or topology changes) are applied, they must be validated first. Invalid configs should be rejected to avoid breaking the mesh. The last known good state should always be retained as a fallback.

### In Short

This section is all about reliability and uptime. Even if parts of the system crash, restart, or lose connectivity, the DMR mesh should recover automatically, continue routing messages safely, and validate changes to avoid bad updates.
