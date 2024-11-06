## Batching inserts for streamed data to db

### Prerequisites
- separate api and db tasks

### Consumer Side Batching
-  consumer processes a batch of tasks if:
	- min size of batch is reached
	- batch_timeout is over

### Celery Problems with User Inserts
#### Why celery grouping won't work
- we don't want the task to retry the whole list of users every time any http exception is received from a single user
- thus, batching must happen after 


### Keeping messages small with compression
For a single row of data however, it might not be worth the computational cost to compress and decompress the data.


### Buffer Table

1. **High-Concurrency Transactions:**
    
    - Use database-level locks to ensure that no two transactions modify the same data concurrently.
2. **Distributed Systems Coordination:**
    
    - Use application-level locks (e.g., Redis) to coordinate access to resources across multiple services or processes.

### Why Async?
- We don't want the program to block while waiting for messages
- although this may still work for when there is only 1 consumer, once there are multiple consumers waiting for messages, async is desired
- sync is required when sequential operations need to be conducted
- sync is more beneficial when tasks are cpu-bound and not io-bound
- https://www.cloudamqp.com/blog/publishing-throughput-asynchronous-vs-synchronous.html
	- opening an amqp connection per message greatly decreases throughput if message ack is required

### If api tasks fail, send the username to a redis set for failed operations

### concurrency and gevent not really needed for tasks waiting on batching in aio pika


## Throttling Celery Tasks
https://github.com/freelawproject/courtlistener/blob/main/cl/lib/celery_utils.py
- celery only provides task level rate limiting, not queue level rate limiting


## PIKA IS NOT THREAD SAFE
## GEVENT IS NOT THREADSAFE FOR REDIS CONNECTIONS


## Alembic
```python
DELETE from alembic_version;
alembic stamp head
alembic revision --autogenerate -m "initial migration"
alembic upgrade head

```


## Kafka vs Pulsar vs Redpanda
My requirements
- asyncio
aiokafka is the only library that supports asyncio
- pulsar is async but not suitable for my use case
- redpanda is much easier to deploy as it only needs to handle one type of node unlike kafka
- redpanda is also compatible with all kafka clients


## Kubernetes control planes
- the control planes chooses where to place nodes based on resource requirements

## My setup
- kubernetes clusters on talos vm's which are immutable os's
- services
	- redpandas cluster
	- some form of s3 cluster

## Async

### Design choice
Combo:
- multiprocess
- async batch
Benefits:
- my proxy provider limits connections
- httpx and async allows connection pooling
- threading will await on only 1 network request and switch to another thread: lots of ipc overhead
- asyncio allows more than 1 network request to be started on a single thread, limit is how much memory you have
- asyncio is very useful especially if latency of network requests are high in my case as requests must be forwarded to a proxy


### Why `httpx` Is Simpler than aiohttp:

- In `httpx`, setting up a proxy for the entire client is much easier, as you only need to specify the `proxies` argument when creating the client.
- `httpx` handles connection pooling by default, which allows the client to reuse the same connection to the proxy across multiple requests, without needing custom connectors.



# Load Balance Messsage Queue
- hash message by user_id
- 