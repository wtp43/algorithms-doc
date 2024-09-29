# Persistent Volumes
- type of network storage
- manages storage class, provides dynamic scaling
- automated provisioning of persistent volumes based on persistent volume claims

## Benefits
- local volumes are tightly coupled to each node. If a Pod moves to a different node (due to a node failure), the data might not be accessible unless explicitly handled
## Use Case
- distributed workloads
- cloud environments
## Use Case for Local Path Storage
> High performance (local disk)
- Static nodes