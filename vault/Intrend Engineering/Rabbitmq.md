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