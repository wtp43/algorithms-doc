# Redpanda


## Basic Setup


### Tune Kubernetes Worker Nodes for Production
- talos doesnt have a direct shell
- deploy a nginx container and access shell this way

```sh
curl -1sLf 'https://dl.redpanda.com/nzc4ZYQK3WRGd9sy/redpanda/cfg/setup/bash.deb.sh' | bash && apt install redpanda -y
```

