# Latency based kubernetes Auto-scaler

**Clone the repository**
```bash
git clone https://github.com/anushiya-thevapalan/latency-based-kubernetes-custom-autoscaler
cd latency-based-kubernetes-custom-autoscaler
```

## Deploy Ballerina based micro-service

**Create the deployment**
```bash
cd deployments
kubectl create -f ballerina-prime-testing.yaml
```

**Expose the deployment using Loadbalancer service**
```bash
kubectl create -f ballerina-prime-testing-svc
```

## Creating roles and role bindings
```bash
cd deployments/roles
kubectl create -f deployments-and-deployements-scale-role-binding.yaml
kubectl create -f deployments-and-deployements-scale.yaml
kubectl create -f endpoints.yaml
```
## Deploying monitoring server

**Create the deployment**
```bash
cd deployments
kubectl create -f monitoring-server.yaml
```

**Expose the deployment using NodePort service**
```bash
kubectl create -f monitoring-server-svc.yaml
```

### Deploying Auto-scaler

```bash
cd deployments
kubectl create -f auto-scaler.yaml
```
