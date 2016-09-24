docker run python:3.5 /bin/echo 'Hello world'

# install minikube

```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.10.0/minikube-darwin-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```


```
$ minikube start
$ kubectl run hello-minikube --image=gcr.io/google_containers/echoserver:1.4 --port=8080
$ kubectl expose deployment hello-minikube --type=NodePort
$ kubectl get pod
$ curl $(minikube service hello-minikube --url)
$ kubectl delete deployment/hello-minikube
```

Create Dockerfile
bulid .
docker tag <sha> dhilipsiva/kubetut:latest

kubectl create -f app-v1.json
kubectl proxy

kubectl describe pod kubetut

```
$ minikube stop
```
