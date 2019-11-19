# latency-based-kubernetes-custom-autoscaler

##### Clone the repository
```bash
git clone https://github.com/anushiya-thevapalan/latency-based-kubernetes-custom-autoscaler
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
kubectl cp auto-scaler /home/auto-scaler
```

#### exec into the monitoring-server pod
```bash
kubectl exec -it monitoring-server bash
```
#### Set required permissions
```bash
cd home/metrics-server/bash
chmod +x *.sh
```
#### Start the monitoring server
```bash
cd bash
./start_autoscaler.sh
```




