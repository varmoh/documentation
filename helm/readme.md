# Combained Chart

#### As example, I am using `ruuter` and `resql`

This Helm chart packages two subcharts: **Ruuter** and **Resql**, allowing you to manage and deploy them together using a single `values.yaml` file.

## Directory Structure

```
byk/
├── Chart.yaml
├── values.yaml
├── charts/
│   ├── ruuter/
│   └── resql/
└── templates/  # remains empty
```

## values.yaml (Parent)

Customize subchart values like this:

```yaml
ruuter:
  replicaCount: 2
  image:
    repository: myregistry/ruuter
    tag: latest

resql:
  replicaCount: 1
  image:
    repository: myregistry/resql
    tag: stable
```

The `parent` valus.yaml contains the info of every other values.yaml content under it.

## Packaging the Chart

```bash
cd byk
helm dependency update
helm package .
```
## custom-values.yaml
Is exactly as `parent` values.yaml, but contains updated info you want to use.

## Installing the Chart

```bash
helm install my-release byk-0.1.0.tgz -f your-custom-values.yaml
```

## Notes

- `Ruuter` and `Resql` are full Helm charts with their own `Chart.yaml`, `values.yaml`, and templates.
- Values passed into the parent chart are scoped per subchart using keys (`ruuter`, `resql`).
