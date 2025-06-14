# Namespace Handling in Argo CD Helm Deployments

When deploying Helm charts via Argo CD, managing Kubernetes namespaces properly is crucial. There are two main ways to handle namespaces:

## 1. Pre-created Namespace

- The Kubernetes namespace must exist before deployment.
- You specify the target namespace in Argo CD’s Application spec (`destination.namespace`).
- The Helm chart deploys resources into this namespace.
- If the namespace doesn’t exist, deployment will fail.

**Example to create namespace manually:**

```bash
kubectl create namespace laupaev
```

## 2. Dynamic Namespace Creation via Helm Chart

- The Helm chart includes a Namespace manifest templated with a value (e.g., {{ .Values.namespace }}).
- The namespace value can be overridden via Argo CD Helm parameters in the API request.
- Argo CD must have RBAC permissions to create namespaces for this to work.
- This allows the namespace to be created automatically during sync.

**How to use namespace parameter with Argo CD API call**

In your Helm chart, have a values.yaml:
```yaml

namespace: placeholder-namespace
```

and a templates/namespace.yaml like:
```yaml

apiVersion: v1
kind: Namespace
metadata:
  name: {{ .Values.namespace }}
```

Then, create the Argo CD Application replacing laupaev2 with the desired namespace:
```bash

curl -k -X POST https://localhost:8081/api/v1/applications \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "metadata": {
      "name": "test-helm-app-2",
      "namespace": "argocd"
    },
    "spec": {
      "project": "default",
      "source": {
        "repoURL": "https://github.com/varmoh/argo-test",
        "path": "test-chart-2",
        "targetRevision": "main",
        "helm": {
          "parameters": [
            {
              "name": "namespace",
              "value": "laupaev2"
            }
          ]
        }
      },
      "destination": {
        "server": "https://kubernetes.default.svc",
        "namespace": "laupaev2"
      },
      "syncPolicy": {
        "automated": {
          "prune": true,
          "selfHeal": true
        }
      }
    }
  }'
```

Important:

- The destination.namespace must match the namespace value passed to the Helm chart.
- Argo CD must have sufficient Kubernetes permissions (RBAC) to create namespaces if using the dynamic creation method.
