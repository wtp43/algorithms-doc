# Talos
## Cluster  Configs
```python
talosctl gen secrets
# kubernetes
talosctl gen config
```

- kubectl is used to manage multiple kubernetes clusters
- talosctl is sued to manage multiple talos clusters
- switching between clusters is done using context which are identified by name
- kubernetes api should be a dns or load balancer placed in front of the control plane nodes of your kubernetes clusters to achieve high availability
- talos provides a VIP(virtual ip address) to load balance control plane nodes. have to use kubernetes end point
- **YAML**: You will still use YAML for managing Talos itself (the OS layer). YAML is the required format for Talos cluster and node configuration.
- **Helm**: You would use Helm to deploy and manage applications on the Kubernetes cluster that Talos is running. Helm could be used to deploy Kubernetes resources (e.g., Pulsar, Prometheus, MinIO), but not Talos OS configuration.
### Control Plane Settings
https://mirceanton.com/posts/2023-11-28-the-best-os-for-kubernetes/
- optional: allow control plane node to be allowed to complete tasks
- disable predictable interface names allows generic configurations
- enable dhcp on eth0 interface
- configure virtual ip
- 
```sh 
# @ specifies yaml and not json
talosctl gen config intrend-cluster https://192.168.50.200:6443 \
  --with-secrets secrets.yaml \
  --config-patch @patches/allow-controlplane-workloads.yaml \
  --config-patch @patches/cni.yaml \
  --config-patch @patches/dhcp.yaml \
  --config-patch @patches/install-disk.yaml \
  --config-patch @patches/interface-names.yaml \
  --config-patch @patches/kubelet-certificates.yaml \
  --config-patch-control-plane @patches/vip.yaml \
  --output rendered/
```

- the controlplane.yaml generated specifies settings for both kubernetes and talos clusters
- worker.yaml is the machine config file for the worker, not the cluster
- the talosconfig file is the equivalent a kube config file in the talos os
	- specifies the api endpoint at which the talos api is available
	- needs to be configured
#### Apply the config to all machines
```sh
talosctl apply -f rendered/controlplane.yaml -n 192.168.50.201 --insecure
talosctl apply -f rendered/controlplane.yaml -n 192.168.50.202 --insecure
talosctl apply -f rendered/controlplane.yaml -n 192.168.50.203 --insecure
```
- --insecure is needed since PKI is not initialized yet
#### Configure talosctl to work with the new cluster

#### Bootstrap Kubernetes
```sh
# use any node in the talos cluster
talosctl bootstrap -n 192.168.50.201
```
- starts etcd

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