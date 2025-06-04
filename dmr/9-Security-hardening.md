## Security and Hardening

This section ensures that the entire DMR system — including clients, DMR nodes, and CentOps — operates in a secure, trustworthy, and auditable way, with protections against misuse or unauthorized access.

### Audit Logging and Tamper Resistance

All sensitive actions — like message rejections, config updates, or certificate changes — must be logged. These logs should be immutable or protected against tampering, providing a reliable trail for auditing and incident response.

### mTLS-Only Comms Enforced Across All Nodes

Every connection — between clients and DMRs, between DMRs themselves, and between DMRs and CentOps — must use mutual TLS (mTLS). This ensures both ends authenticate each other and all traffic is encrypted.

### Token Binding (if Used for Short-Lived Access)

If you use short-lived tokens (e.g., JWTs) for access control, those tokens can be bound to specific TLS sessions or certificates. This prevents stolen tokens from being reused elsewhere, adding a second layer of defense.

### Denylist Revocation Propagation and Enforcement

If a certificate or identity is compromised or no longer trusted, it must be revoked and added to a denylist. All DMR nodes must be able to fetch and apply this denylist in near real-time, immediately cutting off compromised entities from the network.

### In Short

This section locks down the DMR ecosystem, ensuring only trusted actors can connect, all activity is logged for auditing, and security breaches can be quickly responded to through certificate revocation.
