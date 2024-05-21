---
created: ""
---
---


# System Design
https://interviewing.io/
hellointerview.com

https://interviewing.io/guides/system-design-interview/part-two#about-these-15-fundamental-concepts

# System Design Interview Vol: 1
## Scale from Zero to Millions of Users
### Single Server Setup
- User access websites through 3rd party DNS (domain name system)
- IP address is returned to browser
- HTTP request are sent directly to web server
- Web server returns html pages or JSON response for rendering
### Database
#### NoSQL (non-relational db)
- Four categories: key-value stores, graph stores, column stores, document stores
- Join operations generally not supported
- When to use:
	- App requires low latency
	- Data is unstructured/non relational
	- You only need to serialize/deserialize data(JSON,XML,YAML)
		- You need to store a massive amount of data

### Vertical vs Horizontal Scaling
>Vertical scaling or "scale up" is the process of adding more power (CPU, RAM) to your servers. Horizontal scaling or "scale-out" allows you to scale by add more servers into your pool of resources. 
- Vertical scaling is useful when traffic is low
	- Cons: impossible to add unlimited power, does not have failover and redundancy since if one server goes down, the website/app goes down completely
- Horizontal scaling is more desirable for large scale applications
### Load Balancer
- Addresses slow response or failure to connect to server when too many users 
- Users connect to load balancer directly
- Web servers are unreachable directly by clients
- For better security, private IPs are used for communication between servers (only reachable between servers in the same network)
- By adding a load balancer and second server, if server 1 goes offline, all the traffic will be routed to server 2
![Pasted-image-20240312060004.png](</Interview-Prep-2024/attachments/Pasted-image-20240312060004.png>)

### Database Replication
#### Master/slave relationship
- Master database generally only supports write operations
- Slave database gets copies of data from mater database and only supports read operations
- Most applications require higher ratio of reads to write, thus # slave databases > # master databases
- Reliability: No data loss because of replication
- High Availability: Website remains in operation even if one database is offline
- If only one slave database is available and it goes offline, read operations will be directed to the master database temporarily
- If the master database goes offline, a slave database will be promoted to be the new master
	- A new slave database will replace the old one for data replication immediately
	- This also requires the data in a slave to be up to date. The missing data can by updated by running data recovery scripts
#### Other replication methods
- Multi-masters
- Circular replication
### Cache
> Temporary data store layer, much faster than DB
- Better system performance, reduces database workloads, ability to scale cache tier independently
- Read-through cache strategy: if cache does not have requested response, query db, store it in cache, send to user
- Cached data is stored in volatile memory, not ideal for persisting data
- Expiration policy: good practice to implement appropriate expiration policy
- Consistency: keeping data store and cache in sync. Requires invalidating cache when making mutations to data
- Mitigating failures: a single cache server represents a potential SPOF(single point of failure). This can be avoided by using multiple cache servers across different data centers
- Eviction Policy: LRU, LFU, FIFO
### CDN
>Network of geographically dispersed servers used to deliver static content
>CDN servers cache static content like images, videos, css, JS files
- Users are served content from geographically closest CDN
- If the CDN server doesn't have image.png for example in the cache, it will request it from the origin (web server or online storage like Amazon S3), cache it, then return to the user
- The image is returned from the cache as long as the TTL (Time-to-live)
- Same concerns as cache (Expiration policy, fallback policy, invalidating files)
- Invalidating Files
	- Use API provided by CDN vendors
	- Object versioning (serve a different version and append parameter to URL)
### Stateless Web Tier
- To scale web tier horizontally, we need to move state(ie: user session data) out of the web tier
- Store session data in persistent storage: SQL or NoSQL 
#### Stateful Architecture
- Each user's session data is stored in a specific server. 
- To authenticate each user, HTTP requests must be routed to that specific server
- This can be done with sticky sessions in load balancers but adds overhead
#### Stateless Architecture
- A cluster of web servers fetch state data from a shared data store
- NoSQL can be used for easy scaling
- Autoscaling means adding/removing web servers automatically based on traffic load
### Data Centers
- Load Balancer will geoDNS(DNS service allowing domain names to be resolved to IP addresses based on the location of the user) route (geo-route) users to the closest data center
#### Multi-data center setup
 - Traffic redirection: GeoDNS to direct traffic to nearest data center depending on user IP
 - Data Synchronization: Replicate data across multiple data centers
 - Test and deployment: Test website/app at different locations (use automated deployment tools)
### Message Queue (Decoupled)
> Durable component, stored in memory, supports async communication
- Serves as a buffer and distributes async requests
- Input services/Producers/Publishers, create messages and publish them to message queue
- Other services/Servers/Consumers/Subscribers  connect to queue and perform actions defined by messages
- **Decoupling Advantages**:
	- Producer can post message to queue even when consumer is unavailable to process it
	- Consumer can read messages from queue even when producer is unavailable
	- Producers/Consumers can be scaled independently
![Pasted-image-20240312063941.png](</Interview-Prep-2024/attachments/Pasted-image-20240312063941.png>)

### Logging, metrics, automation 
- Logging: can be done at per server level, or use tools to aggregate them to a centralized service
	- Metrics: Host level metrics (CPU, memory, disk I/O), aggregated level metrics (performance of entire database tier, cache tier), business metrics (daily users, retention, revenue)
- Automation: Continuous integration (each code check-in is verified through automation), automate build, test, deploy process

### Database Scaling
#### Vertical Scaling
- Add more CPU/RAM
- Still risk of SPOF
- Powerful servers are much more expensive
#### Horizontal Scaling (Sharding)
- Separate large databases into smaller parts called **shards**
- Data can be allocated to specific server with hash function
- The column(s) used to determine how data is distributed (using the hash function) is called the **Sharding/Partition Key**
	- Criteria: Key must be evenly distributed
##### Resharding Data
Needed when a single shard cannot hold enough data, certain shards might experience shard exhaustion faster than others due to uneven data distribution
- Update shard function and move data around
- Use Consistent Hashing
##### Celebrity Problem
>Excessive access to a specific shard causing server overload
- Allocate a shard for each celebrity
- Each shard might even require further partition
##### Join and de-normalization
>Once a database has been sharded across multiple servers, it is hard to perform join operations across database shards
- De-normalize the database so that queries can be performed in a single table

## Back-Of-The-Envelope Estimation
>Estimate system capacity or performance requirements
- Byte = 8 bits
- ASCII Char = 1 byte
### General Latency Numbers
1 ns = 10^-9 seconds
1 μs= 10^-6 seconds = 1,000 ns
1 ms = 10^-3 seconds = 1,000 μs = 1,000,000 ns
- L1 Cache reference: 0.5 ns
- Branch mispredict: 5 ns
- L2 Cache: 7 ns
- Mutex lock/unlock: 100 ns
- Main Memory reference: 100 ns
- Compress 1K bytes with Zippy: 10 microseconds
- Send 2K bytes over 1 Gbps network: 20 microseconds
- Read 1 MB sequentially from memory: 250 microseconds
- Round trip in same datacenter: 500 microseconds
- Disk seek: 10 ms
- Read 1 MB sequentially from network: 10 ms
- Read 1 MB sequentially from disk: 30 ms 
- Send packet from CA to Netherlands to CA: 150 ms
#### Conclusions
- Memory fast, disk slow
- Avoid disk seeks
- Simple compression algorithms are fast
- Compress data before sending over a network
### Availability Numbers
- 99% availability = 14.40 minutes downtime/day = 3.65 days downtime/year
- 99.9% availability = 1.44 minutes downtime/day = 8.77 hours downtime/year
### Example: Estimate Twitter QPS and storage requirements
#### Assumptions
- 300 million monthly active users
- 50% of users use Twitter daily
- Users post 2 tweets per day on average
- 10% of tweets contain media
- Data is stored for 5 years
#### Estimations:
Query per second (QPS) estimate:
• Daily active users (DAU) = 300 million * 50% = 150 million
• Tweets QPS = 150 million * 2 tweets / 24 hour / 3600 seconds = ~3500
• Peek QPS = 2 * QPS = ~7000
We will only estimate media storage here.
• Average tweet size:
• tweet_id 64 bytes
• text 140 bytes
• media 1 MB
• Media storage: 150 million * 2 * 10% * 1 MB = 30 TB per day
• 5-year media storage: 30 TB * 365 * 5 = ~55 PB
### Interview Prep
- QPS, peak QPS, storage, cache, number of servers
- Write down assumptions
- Precision is not expected, round numbers and approximate to your advantage
## Framework for System Design Interviews
Avoid over-engineering, being narrow minded, stubborn
### Step 1: Understand the problem and establish design scope (3-10 mins)
Don't be afraid to ask questions to help you make the right assumptions
- What specific features are we going to build?
- How many users does the product have?
- How fast does the company anticipate to scape up?
- What are the anticipated scales in 3, 6, 12 months
- What is the company's technology stack?
- What existing services can I leverage to simplify the design?
#### Example
Design a news feed system
- Q: is this a mobile app or web app or both?
- Q: What are the most important features for the product?: Ability to make a post and see friend's feed
### Step 2: Propose high-level design and get buy-in(10-15 mins)
- Come up with initial blueprint and ask for feedback
- Draw box diagrams with key components
- Do back of the envelope calculations to evaluate that blueprint fits the scale constraints
### Step 3: Design Deep Dive (10-25 mins)
- Work with interviewer
- Try not to get into unnecessary details
- Investigate important use cases
### Wrap up (3-5 mins)
- Identify bottlenecks and potential improvements
- Error cases and how they would be handles
- Operation issues: how to monitor metrics error logs, deploy
- How to handle next scale curve
- Propose refinements you need if you had more time

## Rate Limiter
>Controls rate of traffic sent by client
- Reduces cost, prevents DDoS 
- Prevent server overload

### Understand the Problem
What kind of rate limiter are we going to design?
- Client-side vs server-side API limiter
Does the limiter throttle API requests based on IP, user ID, or Other Properties?
- It should be flexible 
What is the scale of the system? Start up or big company?
- Should handle large # requests
**Distributed rate limiting**
Will system work in distributed environment?
- The rate limiter can be shared across multiple servers or processes
Is the rate limiter a separate service or should be implemented in application code?
**Exception Handling**
Do we need to inform users who are throttled?

### High-level design
- Client-side implementation is generally unreliable, client requests can be forged, we also don't always have control over client implementation
- Rate limiter can be either on the api server or implemented as a middleware (API gateway)
	- Takes time to build own rate limiting service vs using commercial API gateway
	- Full control of algorithm if implementing own service
#### Rate Limiting Algorithms
##### Token Bucket 
>Memory efficient, allows burst of traffic for short periods, but challenging to tune bucket size/refill rate properly
- Container with pre-defined capacity
- Tokens refilled at preset rates periodically
- Generally necessary to have different buckets for different API endpoints
	- If we need to throttle requests based on IP addresses, each IP address requires a bucket
![Pasted-image-20240322142254.png](</Interview-Prep-2024/attachments/Pasted-image-20240322142254.png>)
##### Leaking Bucket
>Requests processed at fixed rate
>But bursts of traffic can fill up queue with old requests and if they are not processed in time, recent requests will be rate limited
- Requests added to queue if not full, else dropped
- Requests pulled from queue and processed at regular intervals
- **Bucket size**
- **Outflow rate**: how many requests can be processed at a fixed rate
![Pasted-image-20240322142406.png](</Interview-Prep-2024/attachments/Pasted-image-20240322142406.png>)
##### Fixed Window Counter
- Divides timeline into fix-sized time windows
- Assign counter for each window
- Each request increments counter by one
- Once counter reaches predefined threshold, new requests are dropped until a new time window starts
![Pasted-image-20240322142431.png](</Interview-Prep-2024/attachments/Pasted-image-20240322142431.png>)
**Potential Problem**
- Burst of traffic at edges of time windows can cause more requests than
- Ex: 1 minute windows are allowed 5 requests, but there is 10 allowed here in 1 minute
![Pasted-image-20240322142555.png](</Interview-Prep-2024/attachments/Pasted-image-20240322142555.png>)
##### Sliding Window Log
- Keep track of request timestamps (cached in sorted sets of Redis)
- When new request comes in, remove all outdated timestamps (any timestamps not within the current window)
- Add timestamp of request to log
- Reject request (still keep it's timestamp in log) if log size is greater than allowed count
- Requires a lot of memory to store timestamps 
- Rate limiting very accurate, any rolling window will not exceed rate limit
![Pasted-image-20240322143142.png](</Interview-Prep-2024/attachments/Pasted-image-20240322143142.png>)

##### Sliding Window Counter
- Requests in current window + requests in the previous window * overlap percentage of
the rolling window and previous window
![Pasted-image-20240322143537.png](</Interview-Prep-2024/attachments/Pasted-image-20240322143537.png>)
#### High-level Architecture
- Store counter in cache
- Redis offers INCR and EXPIRE (sets timeout for counter, automatically deleted after)

### Design Deep Dive
#### Rate limiting rules
pg 64

# Overview
## Scaling System
- Keep web tier stateless
- Build redundancy at every tier
- Cache data as much as you can
- Support multiple data centers
- Host static assets in CDN
- Scale data tier by sharding
- Split tiers into individual services (message queues) 
- Monitor system and use automation tools
![Pasted-image-20240312065728.png](</Interview-Prep-2024/attachments/Pasted-image-20240312065728.png>)
- Only one data center is shown but there can be moredd
# Other Topics
## Dynamic content caching

