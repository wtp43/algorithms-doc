# Installation


```sh
helm install --set namespaceCreate=true --set volumes.persistance=false


helm install \  
--values examples/values-one-node.yaml \  
--namespace pulsar \  
apache/pulsar
```