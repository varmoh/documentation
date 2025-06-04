## OPA with DMR

**OPA - Open Policy Agent**

OPA provides a centralized, flexible way to define and enforce complex access control policies for messaging flows. It allows the DMR to make real-time, fine-grained decisions based on:

- Client identity
- Message metadata
- Trust information

This approach keeps policies maintainable, auditable, and easy to update without downtime.

## Developer Concerns

Integrating OPA adds extra complexity and a new service to manage. Key concerns include:

- **Latency:** Policy evaluation might introduce latency and requires careful performance tuning.
- **Learning Curve:** Developers need to learn OPA’s policy language (Rego).
- **Testing and Security:** Ensuring that policies are tested and secure is crucial.
- **Overkill for Simple Use Cases:** For simpler scenarios, OPA could be considered overkill.

```mermaid
flowchart TB
    subgraph DMR_Node[DMR Node]
        Ingress["Ingress Proxy<br/>(nt Envoy)"]
        MetaExtract[Metaandmete eraldus]
        OPA["OPA Autoriseerija<br/>(Local Agent)"]
        Forwarder[Sõnumi edastaja]
        Telemetry[Audit & Log Agent]
    end

    subgraph Central_Management[Centops]
        PolicyStore[Poliitikate hoidla]
        CertMgmt[Sertifikaadihaldus]
    end

    subgraph External_Client[Osapool / Süsteem]
        Client["Client A<br/>(Sõnumi saatja)"]
    end

    Client -->|mTLS ühendus<br/>+ Metaandmed| Ingress
    Ingress --> MetaExtract
    MetaExtract -->|JSON päring| OPA
    OPA -->|ALLOW / DENY| Forwarder
    OPA -->|Audit| Telemetry
    Forwarder -->|Krüptitud sõnum| NextNode[DMR Node B / Sihtsüsteem]

    PolicyStore -->|"Reeglid (pull või push)"| OPA
    CertMgmt -->|CA ja cert'id| Ingress
