### CentOps 

- Kubernetes Cluster: The outer boundary represents the Kubernetes cluster where CentOps operates.

- CentOps (Custom Automation Tool):
  - Go-based Controller: The core automation component, written in Go, that manages deployments, updates the DeploymentHistory CRD, and interacts with the Kubernetes API.

  - Monitoring Service: A Go-based service that exposes metrics (e.g., CPU, error rates) for Prometheus to scrape.

- Kubernetes Resources:
  - Kubernetes API: The interface for all interactions with K8s resources.

  - CRDs (DeploymentHistory): Stores deployment metadata (e.g., version, image) for history and rollback.

  - Deployments: The application workloads managed by CentOps.

- Metrics Infrastructure:
  - Prometheus: Collects and stores metrics from the Monitoring Service.

  - Grafana: Optional visualization of metrics for the user.

- Environments:
  - Local Minikube: Used for building and testing CentOps.

  - Cloud Environment: Production deployment, on a non-AWS/Azure cloud provider.

- User/Operator: Interacts with CentOps via the controller’s API (e.g., to trigger deployments or rollbacks) and monitors metrics via Grafana.

- Interactions:
  - The Controller manages Deployments, updates CRDs, and uses the Kubernetes API.

  - The Monitoring Service exposes metrics to Prometheus, which Grafana visualizes.

  - Both environments (Minikube and Cloud) deploy the Kubernetes Cluster.

  - The User interacts with the Controller and monitors via Grafana.
```mermaid

flowchart TD
    %% Main components within Kubernetes
    subgraph Kubernetes_Cluster["Kubernetes Cluster"]
        direction TB
        
        %% CentOps components
        subgraph CentOps["CentOps (Custom Automation Tool)"]
            Controller["Go-based Controller<br>(Automation Logic)"]
            Monitoring["Monitoring Service<br>(Go-based)"]
        end
        
        %% Kubernetes resources
        K8s_API["Kubernetes API"]
        CRDs["CRDs<br>(DeploymentHistory)"]
        Deployments["Deployments<br>(Application Workloads)"]
        
        %% Metrics infrastructure
        Prometheus["Prometheus<br>(Metrics Storage)"]
        Grafana["Grafana<br>(Optional Visualization)"]
    end
    
    %% Environments
    subgraph Environments
        Minikube["Local Minikube<br>(Build & Test)"]
        Cloud["Cloud Environment<br>(Production)"]
    end
    
    %% External entities
    User["User/Operator"]
    
    %% Interactions
    User -->|Interacts via API| Controller
    Controller -->|Manages| Deployments
    Controller -->|Updates/Queries| CRDs
    Controller -->|Interacts with| K8s_API
    K8s_API -->|Manages| Deployments
    K8s_API -->|Stores| CRDs
    
    Monitoring -->|Exposes Metrics| Prometheus
    Prometheus -->|Visualizes| Grafana
    Monitoring -->|Runs in| Deployments
    
    %% Environment connections
    Minikube -->|Deploys to| Kubernetes_Cluster
    Cloud -->|Deploys to| Kubernetes_Cluster
    User -->|Monitors| Grafana

    %% Styling
    classDef centops fill:#f9a825,stroke:#333,stroke-width:2px;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:2px;
    classDef metrics fill:#28a745,stroke:#333,stroke-width:2px;
    classDef env fill:#e0e0e0,stroke:#333,stroke-width:1px;

    class CentOps centops;
    class K8s_API,Deployments,CRDs k8s;
    class Prometheus,Grafana metrics;
    class Minikube,Cloud env;
