### Flow
- **Action**: Open CentOps → Click "Add Manifest"
- **Form Fields**:
  - **Filename**: `clientA-<timestamp>.yaml`
  - **YAML Entry Box** (example):

```yaml
imagePullSecrets: []
nameOverride: ""
fullnameOverride: ""

podAnnotations: {}

podSecurityContext: {}

securityContext: {}

domain: test.buerokratt.ee 
secretname: ruuter.test.com1106prod 
ingress:
  certIssuerName: letsencrypt-prod  
release_name: "component-byk-ruuter"    

images:
  scope:
    registry: "ghcr.io"
    repository: "buerokratt/ruuter"
    tag: "pre-alpha-test-2.1.8"
  dsl:
    registry: "ghcr.io"
    repository: "buerokratt/buerokratt-dsl"
    tag: "backoffice-module-test-1.1.77" 

env:
  LOGGING_LEVEL_ROOT: "INFO"
  LOG_LEVEL_TIMING: "INFO"
  APPLICATION_LOGGING_DISPLAY_REQUEST_CONTENT: "false"
  APPLICATION_LOGGING_DISPLAY_RESPONSE_CONTENT: "false"
  APPLICATION_CORS_ALLOWED_ORIGINS: https://admin.test.com
```

File is saved, e.g. `clientA-20250611-1458.yaml`

Where ? DB ? S3 ?

Database an Ruuter and Resql

DSL
```
declaration:
  call: declare
  version: 0.1
  description: "Fetch manifest YAML by client and version"
  method: get
  returns: text
  namespace: ruuter

extractRequestData:
  assign:
    client: ${incoming.path.client}
    version: ${incoming.path.version}
    yaml: ${incoming.body}

postManifest:
  call: http.post
  args:
    url: "http://resql-service/centops/post_manifest.sql"
    body:
      client_id: ${client}
      version: ${version}
      yaml: ${yaml}
  result: res
  next: post_result

fetchManifest:
  call: http.post
  args:
    url: "http://resql-service/centops/get_manifest.sql"
    body:
      client_id: ${client}
      version: ${version}
  result: res
  next: get_return_result

post_result:
  return:200
  next: end

get_return_result:
  assign:
    yamlContent: ${res.response.body.rows[0].yaml}
  return: ${yamlContent}
  next: post_argo

post_argo:
  call: http.post
  args:
    url: http://argocd/api?endpoint
    body: ${yamlContent}
  next: end

```
SQL
```

-- Table schema
CREATE TABLE manifests (
  client_id TEXT NOT NULL,
  version TEXT NOT NULL,
  yaml TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  PRIMARY KEY (client_id, version)
);


-- name: postManifest
INSERT INTO manifests (client_id, version, yaml, created_at)
VALUES (:client_id, :version, :yaml, NOW())
ON CONFLICT (client_id, version) DO UPDATE
  SET yaml = EXCLUDED.yaml,
      created_at = NOW();
---

-- name: getManifest
SELECT yaml
FROM manifests
WHERE client_id = :client_id
  AND version = :version;
```

### 2. Helm Chart: Templating Usage

Deployment template example

```
containers:
  - name: ruuter
    image: "{{ .Values.images.scope.registry }}/{{ .Values.images.scope.repository }}:{{ .Values.images.scope.tag }}"
    env:
    {{- range $key, $val := .Values.env }}
      - name: {{ $key }}
        value: "{{ $val }}"
    {{- end }}
```

Ingress Template example

```
spec:
  tls:
    - hosts:
        - {{ .Values.domain }}
      secretName: {{ .Values.secretname }}
  rules:
    - host: {{ .Values.domain }}
```

Path /templates/fetch-manifest-job.yaml  
```
apiVersion: batch/v1
kind: Job
metadata:
  name: fetch-clienta-values
  annotations:
    argocd.argoproj.io/hook: PreSync
    argocd.argoproj.io/hook-delete-policy: HookSucceeded
spec:
  template:
    spec:
      containers:
        - name: fetch-values
          image: curlimages/curl:latest
          command:
            [
              "curl",
              "-s",
              "-o",
              "/workdir/values/clientA.yaml",
              "https://ruuter.test.buerokratt.ee/manifest/clientA/20250611-1458"
            ]
          volumeMounts:
            - name: workdir
              mountPath: /workdir
      restartPolicy: OnFailure
      volumes:
        - name: workdir
          emptyDir: {}
```


Argo application side

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: clientA
  namespace: argocd
spec:
  destination:
    namespace: clientA
    server: https://kubernetes.default.svc
  project: default
  source:
    repoURL: https://github.com/buerokratt/NoOps
    targetRevision: main
    path: charts/ruuter-chart
    helm:
      valueFiles:
        - values/clientA.yaml   # this file will be downloaded dynamically
  syncPolicy:
    automated:
      selfHeal: true
      prune: true
    syncOptions:
      - CreateNamespace=true
  ignoreDifferences: []  # optional, depending on your config

```

Vaultinject

```
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: ruuter-secret
spec:
  secretStoreRef:
    name: vault-prod
    kind: ClusterSecretStore
  target:
    name: {{ .Values.secretname }}
  data:
    - secretKey: DB_PASSWORD
      remoteRef:
        key: secret/data/ruuter/test
        property: password

```

```mermaid
flowchart TD
  subgraph CentOps
    A1[User opens CentOps UI]
    A2[Clicks Add Manifest]
    A3[Enters filename & YAML manifest]
    A4[Save manifest to PostgreSQL via Ruuter DSL]
  end

  subgraph RuuterDSL
    B1["HTTP GET /manifest/{client}/{version}"]
    B2[Extract client & version from path]
    B3[POST to reSQL endpoint with client & version]
    B4[reSQL runs SQL query]
    B5[Return YAML manifest content]
  end

  subgraph ArgoCD_Helm
    C1[PreSync Job runs in Kubernetes]
    C2[Job curls manifest YAML from Ruuter DSL endpoint]
    C3[Saved as values/clientA.yaml in Job volume]
    C4[Helm chart deploys with values/clientA.yaml]
    C5[Deployment uses templated manifests with values]
  end

  subgraph Vault
    D1[ExternalSecret configured in Helm]
    D2[Fetch secrets from Vault]
    D3[Inject secrets into Kubernetes secrets]
  end

  %% Connections
  A1 --> A2 --> A3 --> A4
  A4 --> B1
  B1 --> B2 --> B3 --> B4 --> B5 --> C1
  C1 --> C2 --> C3 --> C4 --> C5
  D1 --> D2 --> D3
  D3 --> C5

  %% Styling
  classDef box fill:#f9f,stroke:#333,stroke-width:1px,color:#000,font-weight:bold;
  class CentOps,RuuterDSL,ArgoCD_Helm,Vault box;





