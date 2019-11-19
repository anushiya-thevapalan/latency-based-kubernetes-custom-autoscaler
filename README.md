# latency-based-kubernetes-custom-autoscaler

##### Clone the repository
```bash
git clone https://github.com/anushiya-thevapalan/latency-based-kubernetes-custom-autoscaler
```
```bash
cd latency-based-kubernetes-custom-autoscaler
```

## Deploy Ballerina based micro-service

#### Create the deployment
```bash
cd deployments
kubectl apply -f ballerina-prime-testing.yaml
```

#### Expose the deployment using Loadbalancer service
```bash
kubectl apply -f ballerina-prime-testing-svc
```

## Creating roles and role bindings
```bash
cd deployments/roles
kubectl apply -f deployments-and-deployements-scale-role-binding.yaml
kubectl apply -f deployments-and-deployements-scale.yaml
kubectl apply -f endpoints.yaml
```
## Deploying monitoring server

#### Create the deployment
```bash
cd deployments
kubectl apply -f monitoring-server.yaml
```
#### Copy the required files into the pod
```bash
kubectl cp 



