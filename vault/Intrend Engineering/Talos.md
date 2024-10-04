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
  --config-patch @patches/longhorn-config.yaml \
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

### Config
```sh
mkdir -p ~/.talos 
cp rendered/talosconfig ~/.talos/config
```
### Commands
```sh
# get contexts
talosctl config contexts

# update endpoints
talosctl config endpoint 100.104.14.94 100.109.231.59 100.106.232.65 192.168.50.201 192.168.50.202 192.168.50.203

# bootstrap kubernetes
talosctl bootstrap -n talos-01

# get members by passing in ip of any controlplane node
talosctl get members -n talos-01

# fetch kubeconfig of the cluster 
talosctl kubeconfig -n talos-01

# show pods
kubectl get pods -o wide

# get services kubectl get services
kubectl get services
```

## If rolling back vm and error is
error executing bootstrap: rpc error: code = Unavailable desc = last connection error: connection error: desc = "transport
: authentication handshake failed: tls: failed to verify certificate: x509: certificate has expired or is not yet valid: c
urrent time 2024-09-28T13:24:47-04:00 is after 2024-09-28T00:40:10Z"

- re-generate secrets.yaml from new config
https://discuss.kubernetes.io/t/unable-to-connect-to-the-server-x509-certificate-has-expired-or-is-not-yet-valid/16484/4
```sh
talosctl gen secrets --from rendered/controlplane.yaml -o secrets.yaml
rm -rf ~/.talos
```
## In Case of Emergency, Break Glass, Remove Failed Node, Then Add New Node

Superficially, adding a new node and then removing the failed node seems the same as removing the failed node then adding a new one. However, the risks are greater in the former case.

To see why this is so, consider a simple 3-node cluster. A 3-node cluster will have a quorum of 2. If one node fails, the etcd cluster can keep working with its remaining two nodes. However, if you now add a new node to the cluster, quorum will be increased to 3, as the cluster is now a 4-node cluster, counting the down node, and we need more than half available to prevent split brain.

If the new member was misconfigured, and cannot join the cluster, you now have two failed nodes, and the cluster will be down and not recoverable: there will only be two nodes up, and a required quorum of 3.

```sh
talosctl -n <ip> reset
kubectl delete node <node-name>
```


## Extensions and Tailscale
- tailscale configuration: https://www.youtube.com/watch?v=wjDtoe-CYoI&t=500s
```sh
talosctl get extensions -n 192.168.50.203

# Check logs for tailscale and login
talosctl logs ext-tailscale -f -n 192.168.50.203  

k get pods -n kube-system
```


## Longhorn
- Talos specific settings: https://longhorn.io/docs/1.8.0/advanced-resources/os-distro-specific/talos-linux-support/#requirements  
- Install with helm: https://longhorn.io/docs/1.7.1/deploy/install/install-with-helm/
- Longhorn-ingress/Enable UI from outside cluster: https://longhorn.io/docs/1.8.0/deploy/accessing-the-ui/longhorn-ingress/
- expose port
```sh
k apply -f services/longhorn-ingress.yaml
kubectl -n longhorn-system get ingress

```
## Namespaces
```sh
kubectl get namespace <namespace-name> --show-labels
```

### Longhorn Requires Pod Security `enforce: privileged`
```sh
kubectl label namespace longhorn-system pod-security.kubernetes.io/enforce=privileged

```
### Longhorn Ingress
```sh
kubectl -n longhorn-system get ingress
```


## Cilium

### Hubble: Disable ipv6
```sh
helm upgrade --install cilium cilium/cilium --namespace kube-system -f services/hubble.yaml
# must enable on restart
cilium hubble enable
```