# Redpanda


## Basic Setup


### Tune Kubernetes Worker Nodes for Production
- talos doesnt have a direct shell
- deploy a nginx container and access shell this way


```sh
# enter shell container
kubectl get all -l app=nginx
kubectl exec -it mynginx-id -- /bin/bash
curl -1sLf 'https://dl.redpanda.com/nzc4ZYQK3WRGd9sy/redpanda/cfg/setup/bash.deb.sh' | bash && apt install redpanda -y
rpk redpanda mode production
rpk redpanda tune all
rpk iotune
# io config is at /etc/redpanda/io-config.yaml

# if namespace is already in use
helm upgrade --install
helm install --replace
helm ls --all-namespaces
helm ls --namespace cattle-system

kubectl get namespaces
kubectl delete namespace kuberhealthy
kubectl create namespace kuberhealthy

kubectl get all -n redpanda

helm uninstall redpanda-controller -n redpanda
kubectl delete all --all -n redpanda
kubectl delete namespace redpanda
```
Changes to the Linux kernel are not persisted. If a worker node restarts, make sure to run `sudo rpk redpanda tune all` on it again.

You can use a privileged DaemonSet to schedule the autotuner on each worker node that runs a Redpanda broker. Apply taints to Nodes that successfully complete the autotuner command. Use tolerations on your Pods so that they are scheduled only on tuned worker nodes.


## Deploy Redpanda with helm only
```sh
helm repo add redpanda https://charts.redpanda.com
helm install redpanda redpanda/redpanda \
  --version 5.9.4 \
  --namespace redpanda \
  --create-namespace \
  --values redpanda-values.yaml \

# Watch cluster status
kubectl --namespace redpanda rollout status statefulset redpanda --watch
```


## Helm and Controller

```sh
helm list -n redpanda
helm uninstall redpanda-controller -n redpanda
```

- `kubectl edit namespace <namespace>`

```sh
helm upgrade --install redpanda-controller redpanda/operator \
  --namespace redpanda \
  --set image.tag=v2.2.4-24.2.5 \
  --create-namespace
  
kubectl apply -f redpanda-cluster.yaml --namespace redpanda
kubectl get redpanda --namespace redpanda --watch
```


```sh
kubectl logs -n redpanda <pod-name>
kubectl describe -n redpanda pod <pod-name>


# MountVolume.SetUp failed for volume 'kafka-default-cert' : secret 'redpanda-default-cert' not found
kubectl get secrets -n <namespace>

kubectl exec -it <pod-name> -- ping <docker-container-ip>


```