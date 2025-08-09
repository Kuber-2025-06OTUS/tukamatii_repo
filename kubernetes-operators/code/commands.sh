eval $(minikube docker-env)

docker build -t redis-operator:latest .

kubectl apply -f redisinstance-crd.yaml

kubectl apply -f rbac.yaml
kubectl apply -f operator-deployment.yaml

kubectl apply -f redisinstance.yaml


kubectl get deployments
kubectl get services
kubectl get pods


kubectl run -it --rm redis-client --image=redis -- bash
redis-cli -h redis-my-redis
ping

kubectl delete -f redisinstance.yaml


kubectl get deployments
kubectl get services