### Команда установки Арго
helm upgrade --install -f kubernetes-gitops/helm-values.yaml  argo argo/argo-cd -n argocd --create-namespace