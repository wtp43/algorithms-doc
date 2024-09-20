# Pulsar

## Overview![Pulsar architecture diagram](https://pulsar.apache.org/assets/images/pulsar-system-architecture-6890df6b0c59a065a56492659ba87933.png)

- A Pulsar instance is composed of one or more Pulsar clusters
- 1+ brokers
	- load balances incoming messages
	- dispatches messages
	- communicates with Pulsar configuration
- BookerKeeper instance (bookies)
	- relies on cluster-specific ZooKeeper cluster for certain tasks
- A BookKeeper cluster consisting of one or more bookies handles persistant storage of messages
- A ZooKeeper cluster specific to that cluster handles coordination tasks between Pulsar Clusters

- it might be possible for separate pulsar clusters to share one bookkeeper cluster (reducing hardware footprint)
- traditionally: a single pulsar cluster and a single bookkeeper cluster
	- https://streamnative.io/blog/pulsar-isolation-part-iii-separate-pulsar-clusters-sharing-single-bookkeeper-cluster
![](https://cdn.prod.website-files.com/639226d67b0d723af8e7ca56/63be7597d526b7b3facbda87_screen-shot-2022-01-12-at-3.27.46-pm.png)


## Brokers
- Stateless component responsible for running the two components below

### HTTP server 
- exposes a REST API for admin tasks and topic lookup and topic lookup for prod/cons
### Dispatcher
- async TCP server over custom binary protocol used for all data transfers
- messages are typically dispatched out of a managed ledger cache (better performance)
	- if backlog exceeds cache: broker will start reading from bookkeeper

## Pulsar Instance
Consists of 
- one or more brokers
- Zookeeper quorum: for cluster-level configuration and coordination
- Ensemble of bookies

## Ledgers
- Append-only data structure with a single writer assigned to multiple bookkeeper storage nodes or bookies
- Bookkeeper guarantees read consistency in ledgers in presence of failures
### Multiple Ledgers
> reasons why
- after a failure, a ledger is no longer writable and a new one needs to be created
- a ledger can be deleted when all cursors have consumed the message it contains: allowing for periodic rollover of ledgers
## Pulsar client
- main entry point for applications to interact with a pulsar cluster
## Pulsar Proxy
- Provides clients a way to interact with Pulsar cluster by connecting them to pulsar message brokers directly