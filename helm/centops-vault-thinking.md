#### initial idea


Before deploying this chart, create the Vault token secret:

```bash
kubectl apply -f vault-token-secret.yaml
# OR
kubectl create secret generic vault-token-secret \
  --namespace default \
  --from-literal=vault-token=your-actual-root-token
```

```bash
kubectl apply -f vault-unseal-key-secret.yaml
# OR
kubectl create secret generic vault-unseal-key \
  --namespace default \
  --from-literal=vault-unseal-key=your-actual-unseal-key
```


### Followup thinking - 0907

After deployment -   

Get the Vault pod name:
`VAULT_POD=$(kubectl get pod -n default -l app=vault -o jsonpath="{.items[0].metadata.name}")`

init vault  
`kubectl exec -it $VAULT_POD -n default -- vault operator init -key-shares=1 -key-threshold=1`

#### save output for now somewhere  

`
Unseal Key: <your-unseal-key>
Initial Root Token: <your-root-token>
`

#### store in kubernets secrets
`
kubectl create secret generic vault-unseal-secret --namespace default --from-literal=unseal-key=<your-unseal-key>
kubectl create secret generic vault-token-secret --namespace default --from-literal=vault-token=<your-root-token>
`

#### unseal vault

delete and recreate job (not sure if this exaple is a good one though yet, it should work but have to test)

`
kubectl delete job vault-unseal -n default
helm upgrade myapp-release ./CentOps-0.1.0.tgz --namespace default
`

#### verify

`
kubectl get job vault-unseal -n default
kubectl logs -n default -l job-name=vault-unseal
`

#### confirm that is unsealed

`
kubectl exec -it $VAULT_POD -n default -- vault status
`

#### Login

`
kubectl exec -it $VAULT_POD -n default -- vault login <your-root-token>
`

#### UI

`
kubectl port-forward svc/vault 8200:8200 -n default
`

#### Enable secret engine

`
kubectl exec -it $VAULT_POD -n default -- vault secrets enable -path=secret kv
`

#### verify

`
kubectl exec -it $VAULT_POD -n default -- vault secrets list
`

#### Add secrets to vault

```
kubectl exec -it $VAULT_POD -n default -- vault kv put secret/resql \
  sqlms_datasources_0_name="centops" \
  sqlms_datasources_0_jdbcUrl="jdbc:postgresql://database:5432/centops_db" \
  sqlms_datasources_0_username="byk" \
  sqlms_datasources_0_password="01234"

kubectl exec -it $VAULT_POD -n default -- vault kv put secret/resql-users \
  sqlms_datasources_0_name="users" \
  sqlms_datasources_0_jdbcUrl="jdbc:postgresql://database:5432/users_db" \
  sqlms_datasources_0_username="byk" \
  sqlms_datasources_0_password="01234"

kubectl exec -it $VAULT_POD -n default -- vault kv put secret/database \
  POSTGRES_USER="byk" \
  POSTGRES_PASSWORD="01234" \
  POSTGRES_MULTIPLE_DATABASES="users_db,centops_db"

kubectl exec -it $VAULT_POD -n default -- vault kv put secret/tim-postgresql \
  POSTGRES_USER="tim" \
  POSTGRES_PASSWORD="123" \
  POSTGRES_DB="tim" \
  POSTGRES_HOST_AUTH_METHOD="trust"
```

### verifu vault agent secrets

#### check configmap

`
helm template myapp-release ./CentOps --namespace default | grep -A 20 "metadata.name: vault-config" > vault-config-rendered.yaml
`

#### veryfy secrets pod

`
DATABASE_POD=$(kubectl get pod -n default -l app=database -o jsonpath="{.items[0].metadata.name}")
kubectl exec -it $DATABASE_POD -n default -c vault-agent -- cat /vault/secrets/database.env
`

EXPECTED OUTPUT:
```
POSTGRES_USER=byk
POSTGRES_PASSWORD=01234
POSTGRES_MULTIPLE_DATABASES=users_db,centops_db
```
