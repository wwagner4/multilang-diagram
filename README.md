# project

## Project setup
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
### Lints and fixes files
```
cd vuegui/
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


### Start server
```
cd multilangdia/
flask run
```

### Docker

```
docker build -t multilang-diagram .
```

#### run
```
docker run --network host -t multilang-diagram
```

```
docker-compose up
```

### Kubernetes

```
eval $(minikube -p minikube docker-env)
minicube start
```

Have 'imagePullPolicy: Never' defined in your deployment.


```
kubectl create -f k8s/d_server.yml
kubectl delete -f k8s/d_server.yml
```

```
kubectl get all
```
