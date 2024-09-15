# Managing Clusters

## Tailscale

### Worker  Machines
```bash
sudo tailscale up --advertise-routes=true --ssh
```
- advertise-routes allows this device to route through subnet routers to 
### Subnet Router
- For proxy server
```shell
tailscale down
tailscale up --reset

tailscale up --accept-dns --advertise-connector --advertise-tags=tag:proxy --accept-routes
tailscale set --advertise-routes=192.168.1.0/24,0.0.0.0/24 
```
- something weird might be going on when advertising routes before advertising connectors
- app connector may be overwritten...
- do a --reset separate from other commands
- advertise connectors first and then do, tailscale set --advertise-routes ...0/
- if this all fails, the config may be bugged and removing the machine from the tailscale network and re-adding it should fix subnet routing 
### Tailscale SSH
- ubuntu ships with firewall tool UFW
- enable the ssh port :`sudo ufw allow ssh`
- generate private ssh key:  `ssh-keygen`
- Allow pubkeyauthentication and authorizedkeysfile: `sudo vim /etc/ssh/sshd_config`
- Copy public key of client to destination: `ssh-copy-id valid_user@host`
- ssh with: `ssh valid_user@host`, `-X` allows X11 forwarding (enabling bidirectional clipboard)
### Proxy Server: Huawei USB modeswitch
```shell
# in /lib/udev/rules.d/40-usb_modeswitch.rules
ATTR{idVendor}=="12d1", ATTR{idProduct}=="1f01", RUN+="usb_modeswitch '%k'"

```

## Docker
> Containerize applications

### Docker compose
- Python requests 2.31 breaks docker compose
- #### **Use `--break-system-packages` to install packages with `pip` in the system-managed Python environment
```shell
sudo pip3 install requests==2.29.0 --break-system-packages

https://stackoverflow.com/questions/64952238/docker-errors-dockerexception-error-while-fetching-server-api-version/68968809#68968809

sudo pip3 install requests==2.29.0 --break-system-packages

```

#### Volumes
- Allows data persistence/sharing and easy access directly from host
### Docker File
- Docker files are not needed if using pre-built images


### Rabbitmq
- allow incoming connections through ufw
- enable port forwarding in debian
```shell
sudo ufw allow 5672/tcp
sudo ufw allow 15672/tcp
sudo ufw status

# uncomment this in /etc/sysctl.conf
net.ipv4.ip_forward=1
#Apply changes without rebooting
sudo sysctl -p 
```

```shell
sudo docker-compose -p rabbitmq_app up --build -d
```
## Kubernetes
> Scaling nodes and managing clusters

### Installation
```shell
sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io sudo systemctl enable docker sudo systemctl start docker
sudo apt update && sudo apt install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update
sudo apt install -y kubelet kubeadm kubectl


# Kubernetes requires swap to be disabled 
sudo swapoff -a
# this does not persist unless the swap entry in /etc/fstab is commented out
```

### Initialize Master Node
```shell
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
```

## Prometheus


## Grafana

