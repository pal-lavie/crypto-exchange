# crypto-exchange
API Platform for  Crypto Exchange 

## About

This is a basic Crypto Exchange API Platform which facilitates creating orders for crypto currency exchange.
The API is created using python flask and can be deployed locally using docker-compose.
I've also provisioned a local kubernetes cluster using minikube using 1 replice for both application service and postgres db service.


## Build and Run Locally

Build the application locally:

```
$ docker compose build
$ docker compose up -d
```


Test locally:

Get all orders:
```
curl --location 'http://localhost:5000/getOrders'

```

Get orders by id:
```
curl --location 'http://localhost:5000/getOrderById/9'

```

Create order:
```
curl --location 'http://localhost:5000/createOrder' \
--header 'Content-Type: application/json' \
--data '
{
            "currency_pair": "ETH-INR",
            "id": 5,
            "order_type": "buy",
            "price": 1200000.0,
            "quantity": 1.0
        }'

```

Update order:
```
curl --location --request PUT 'http://localhost:5000/updateOrder' \
--header 'Content-Type: application/json' \
--data '
{
            "currency_pair": "ETH-INR",
            "id": 5,
            "order_type": "buy",
            "price": 2400000.0,
            "quantity": 2.0
        }'
```

## Kubernetes

Provision a Kubernetes cluster via minikube
```
minikube start
minikube docker-env
```

Create a deployment
```
kubectl apply -f deployment.yml

service/crypto-exchange-service unchanged
configmap/postgres-config unchanged
deployment.apps/postgres-deployment unchanged
persistentvolumeclaim/postgres-pv-claim unchanged
service/postgres-service unchanged
```

View the deployment
```
kubectl get deployment
NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
crypto-exchange       1/1     1            1           8h
postgres-deployment   1/1     1            1           8h
```

View the serive
```
kubectl get service    
NAME                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
crypto-exchange-service   LoadBalancer   10.101.188.27   <pending>     5000:31197/TCP   8h
kubernetes                ClusterIP      10.96.0.1       <none>        443/TCP          8h
postgres-service          NodePort       10.102.47.136   <none>        5432:31876/TCP   8h
```

View the pods
```
kubectl get pods
NAME                                   READY   STATUS    RESTARTS        AGE
crypto-exchange-67bfcc4685-d54zw       1/1     Running   4 (7m50s ago)   8h
postgres-deployment-5d5ffd5884-rbh6m   1/1     Running   1 (8m22s ago)   8h
```

Access application on minikube
```
minikube service crypto-exchange-service
```