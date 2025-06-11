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

fetchManifest:
  call: http.post
  args:
    url: "http://resql-service/centops/manifest_get.sql"
    body:
      client_id: ${client}
      version: ${version}
  result: res

return_result:
  assign:
    yamlContent: ${res.response.body.rows[0].yaml}
  return: ${yamlContent}
  next: end?

```
SQL
```
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
  name: ruuter-clientA
  namespace: argocd
spec:
  destination:
    namespace: ruuter-clientA
    server: https://kubernetes.default.svc
  project: default
  source:
    repoURL: https://github.com/buerokratt/ruuter-deploy
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





