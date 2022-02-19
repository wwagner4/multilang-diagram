# project

## Vue Project setup
```
cd vuegui/
npm install
```

### Compiles and hot-reloads for development
```
cd vuegui/
npm run serve
```

### Compiles and minifies for production
```
cd vuegui/
npm run build
```

## Start server
```
cd multilangdia/
flask run
```

## Docker

```
docker build -t multilang-diagram/windchill .
```

```
docker run --network host  -t multilang-diagram/windchill
```

```
docker-compose up
```

### Kubernetes

```
eval $(minikube -p minikube docker-env)
minikube start
```

Have 'imagePullPolicy: Never' defined in your deployment.


```
kubectl create -f k8s/server.yml
kubectl delete -f k8s/server.yml
```
```
kubectl create -f k8s/nodeport.yml
kubectl delete -f k8s/nodeport.yml
```

```
kubectl get all
```
