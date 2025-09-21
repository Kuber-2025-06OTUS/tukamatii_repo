# Установка Consul в режиме высокой доступности с использованием Helm
helm upgrade --install -f kubernetes-vault/consul-helm-values.yaml  consul ./kubernetes-vault/consul/ -n vault --create-namespace

# Установка Vault в режиме высокой доступности с использованием Helm
helm install vault kubernetes-vault/vault/ -f kubernetes-vault/vault-ha-values.yaml -n vault

# Создание роли аутентификации Kubernetes в Vault для сервис-аккаунта vault-auth
vault write auth/kubernetes/role/otus \
  bound_service_account_names=vault-auth \
  bound_service_account_namespaces=demo \
  policies=otus-pol \
  ttl=1h \
  alias_name_source=serviceaccount_name

# Установка External Secrets Operator c CRD
helm repo update
helm repo add external-secrets https://charts.external-secrets.io
helm install external-secrets \
   external-secrets/external-secrets \
    -n external-secrets \
    --create-namespace \
    --set installCRDs=true
