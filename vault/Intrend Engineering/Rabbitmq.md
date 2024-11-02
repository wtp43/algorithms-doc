# Rabbitmq 

`Producer -> [Channel] -> [Exchange] -> [Queue] -> [Channel] -> Consumer`
## Features
- Exclusive queues: used only by 
	- useful for reply-to queues in a RPC setup
	- temporary task processing
- Topics: message matching by consumers
- 
## Routing Key
- acts as filter for routing messages to one or more queues based on binding rules
## Functools.partial: passing parameters to callback
https://github.com/pika/pika/issues/1283
## consumer has been cancelled server side
- rabbitmq replica node moves to a different machine in kubernetes
https://github.com/mosquito/aiormq/issues/187


## Keepalive in httpx client increases speed


# Performance Optimization

- Queues are single threaded resources
- https://www.rabbitmq.com/blog/2011/09/24/sizing-your-rabbits
## Quorum Queues 

A quorum queue can sustain a 30000 message throughput (using 1kb messages), while offering high levels of data safety, and replicating data to all 3 nodes in a cluster. Classic mirrored queues only offer a third of that throughput and provide much lower levels of data safety.

https://stackoverflow.com/questions/58748684/rabbitmq-message-persistency-difference-between-lazy-queue-and-persistent-deli
To clarify, the `durable` parameter for exchanges and queues does not affect _**individual**_ message persistence. The `durable` parameter ensures that those exchanges and queues survive broker restarts. True, if you have a non-durable queue with persistent messages, and restart the broker, that queue and those messages will be lost, so the `durable` parameter is important.


You should use the `persistent` flag, even with lazy queues. Why? Because you should also be using [Publisher Confirms](https://www.rabbitmq.com/confirms.html#when-publishes-are-confirmed), and a message will only be confirmed when written to disk when `persistent` is set.

## Stream Queues
- good when there are large backlogs
## Implementing Consistent Hashing in RabbitMQ

Implementing consistent hashing in RabbitMQ involves the use of a consistent hashing exchange. This is a type of exchange that [routes messages](https://www.alibabacloud.com/en/product/message-service?_p_lc=1) to queues based on a hash of the routing key. It's an efficient way to distribute messages evenly across several queues, and subsequently, across several RabbitMQ nodes.

When a new message arrives at the consistent hashing exchange, it is routed to a queue based on the hash of its routing key. This ensures that the distribution of messages remains consistent even when queues are added or removed. As a result, the system can scale smoothly without major disruptions or imbalances in the distribution of messages.

### Dead lettering

A queue that is declared with the _x-dead-letter-exchange_ property will send messages which are either rejected, nacked or expired (with TTL) to the specified dead-letter-exchange. If you specify _x-dead-letter-routing-key_ the routing key of the message with be changed when dead lettered.

# Acknowledging every N messages

Secondly, consider not acknowledging every message, but instead acknowledging every N messages and setting the `multiple` flag on the acknowledgement. When the queue is overloaded, it's because it has too much work to do (profound, I know). As a consumer, you can reduce the amount of work it has to do by ensuring you don't flood it with acknowledgements. Thus, for example, you set the `basic.qos` prefetch to 20, but you only send an acknowledgement after you've processed every 10 messages and you set the `multiple` flag to true on the acknowledgement. The queue will now receive one-tenth of the acknowledgements it would have previously received. It will still internally acknowledge all ten messages, but it can do it in a more efficient way if it receives one acknowledgement that accounts for several messages, rather than lots of individual acknowledgements. However, if you're only acknowledging every N messages, be sure that your `basic.qos` prefetch value is higher than N. Probably at least 2*N. If your prefetch value is the same as N, then your consumer will once again be left idle whilst the acknowledgement makes its way back to the queue and the queue sends out a fresh batch of messages.


## Separate Channels for Separate Threads

## Use Channel Pool
- reduce overhead associated with creating and closing channels