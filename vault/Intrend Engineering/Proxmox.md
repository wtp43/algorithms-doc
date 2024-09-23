# Proxmox



## Setup

### On single drive VM
- delete lvm
- https://www.youtube.com/watch?v=tbOe_-XJQS8
```sh
lvremove /dev/pve/data
lvresize -l +100%FREE /dev/pve/root
resize2fs /dev/mapper/pve-root
```

### Making a Cluster
- save configs of existing vms
- delete them
- create cluster, join cluster 
- note: at least half the nodes are required to be running in the cluster to meet default quorom and be able to access the control panel
### Promox host + vm's

### No subscription
```sh
# disable enterprise updates
sed -i 's:^deb :#deb :g' /etc/apt/sources.list.d/pve-enterprise.list

# use no-subscription apt source

#File /etc/apt/sources.list.d/ceph.list

deb http://download.proxmox.com/debian/ceph-reef bookworm no-subscription

#File /etc/apt/sources.list.d/ceph.list

deb http://download.proxmox.com/debian/ceph-quincy bookworm no-subscription

#### File /etc/apt/sources.list
deb http://ftp.debian.org/debian bookworm main contrib
deb http://ftp.debian.org/debian bookworm-updates main contrib

# Proxmox VE pve-no-subscription repository provided by proxmox.com,
# NOT recommended for production use
deb http://download.proxmox.com/debian/pve bookworm pve-no-subscription

# security updates
deb http://security.debian.org/debian-security bookworm-security main contrib
```

## Tailscale directly on host
https://www.youtube.com/watch?v=VlHfc2bGucM

```sh
curl -fsSL https://tailscale.com/install.sh | sh
```

## Ballooning
- reclaim unused ram from vm


## Kubernetes 
https://www.reddit.com/r/homelab/comments/1ceikok/kubernetes_on_proxmox_does_it_make_sense/

https://www.reddit.com/r/Proxmox/comments/1bsk0gq/kubernetes_with_proxmox/
https://www.reddit.com/r/homelab/comments/1enccm8/talos_kubernetes_on_proxmox_using_opentofu/



## Talos OS on Proxmox
https://www.youtube.com/watch?v=MyxigW4_QFM&t=83s


https://www.reddit.com/r/homelab/comments/1faqgs4/proxmox_vs_kubernetes_for_cluster/