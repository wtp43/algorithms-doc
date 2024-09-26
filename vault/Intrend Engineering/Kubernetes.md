# K8s 

## kubectl

##

## Control Plane
 -  manages state of cluster
 - prod: runs on multiple nodes

## Worker  Nodes
- runs the containerized application workloads
- containerized applications run inside a pod
- Worker can have multiple pods
- pods are the smallest deployable units in kubernetes
- pod has multiple containers
- pod provides shared storage and networking for these containers



![Components of Kubernetes](https://kubernetes.io/images/docs/components-of-kubernetes.svg)

## Namespaces
- cluster can have multiple namespaces
- divides cluster resources




## Access a Container's Shell Using Kubectl Exec
## Create  a deployment
```sh
kubectl create deployment mynginx --image=nginx
kubectl get pods

# Open & access container's shell
kubectl exec -it mynginx-56766fcf49-4b6ls -- /bin/bash

```


## DaemonSet

```sh
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd-elasticsearch
  namespace: kube-system
  labels:
    k8s-app: fluentd-logging
spec:
  selector:
    matchLabels:
      name: fluentd-elasticsearch
  template:
    metadata:
      labels:
        name: fluentd-elasticsearch
    spec:
      tolerations:
      # these tolerations are to have the daemonset runnable on control plane nodes
      # remove them if your control plane nodes should not run pods
      - key: node-role.kubernetes.io/control-plane
        operator: Exists
        effect: NoSchedule
      - key: node-role.kubernetes.io/master
        operator: Exists
        effect: NoSchedule
      containers:
      - name: fluentd-elasticsearch
        image: quay.io/fluentd_elasticsearch/fluentd:v2.5.2
        resources:
          limits:
            memory: 200Mi
          requests:
            cpu: 100m
            memory: 200Mi
        volumeMounts:
        - name: varlog
          mountPath: /var/log
      # it may be desirable to set a high priority class to ensure that a DaemonSet Pod
      # preempts running Pods
      # priorityClassName: important
      terminationGracePeriodSeconds: 30
      volumes:
      - name: varlog
        hostPath:
          path: /var/log

```
A DaemonSet defines Pods that provide node-local facilities. These might be fundamental to the operation of your cluster, such as a networking helper tool, or be part of an add-on.