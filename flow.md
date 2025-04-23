```mermaid
graph TD
    A[Start: Incoming Message] --> B[Receive Message in Buerokratt]
    B -->|Route to DMR| C[DMR: Message Proxy Network]
    
    %% DMR Process
    C --> D[Validate Permissions]
    D --> E[Route Message Securely]
    E --> F[Log Interaction Metadata]
    F --> G[Forward Message or Response]
    
    %% CentOps Integration
    C -->|Infrastructure Support| H[CentOps: CI/CD & Operations]
    H --> I[Build & Test via GitHub Actions]
    I --> J[Package as Docker Containers]
    J --> K[Deploy to Kubernetes]
    K --> L[Monitor & Scale DMR Instances]
    L -->|Feedback to DMR| C
    
    %% Response Flow
    G --> M[Deliver Response to Recipient]
    M --> N[End: Message Processed]
    
    %% CentOps Monitoring Loop
    L -->|Issues Detected| O[Auto-Scale or Alert]
    O --> H
    
    %% Styling
    classDef dmr fill:#f9f,stroke:#333,stroke-width:2px;
    classDef centops fill:#bbf,stroke:#333,stroke-width:2px;
    class C,D,E,F,G dmr;
    class H,I,J,K,L,O centops;
