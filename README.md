# latency-based-kubernetes-custom-autoscaler

## Deploy ballerina-prime-testing
### Create the Ballerina-prime deployment
```bash
cd deployments
kubectl apply -f ballerina-prime-testing.yaml
```

### Expose it using Loadbalancer
```bash
kubectl apply -f ballerina-prime-testing-svc
```

## Creating roles and role bindings
```bash
cd deployments/roles
kubectl apply -f deployments-and-deployements-scale-role-binding.yaml
kubectl apply -f deployments-and-deployements-scale.yaml
kubectl apply endpoints.yaml
```



