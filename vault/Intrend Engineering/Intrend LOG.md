## Networking

- A simple proxy such as 3proxy is not sufficient to allow devices from the internet to connect to it
- This is because Phone Carriers use CarrierGradeNAT (to conserve IP addresses) preventing inbound connections such as port forwarding
	- tried cloudflare tunnelling, didn't work. unknown as to why it is unable to tunnel the proxy, works for other http requests such as a request to an api
- used tailscale vpn instead
- set my server using a 4g usb modem connection as an app connector
- on my api which is hosted on a digital ocean VPS, it routes all requests with instagram.com hostname to the app connector 
- this allows me to mask my ip from the VPS 


- when the VPS receives a "log in required" or other rate limiting error, a request to rotate the IP is sent to the 4g server running a fastapi server listening on port 8000

### Experimenting with Instagram Rate Limiting and Carrier IP Range
- to find out more about the ip range that mobile carrier allocates for users, we will log all ip addresses we've seen
	- the result is that ....

- To experiment with rate limiting, we can try different request timings
	- continuous requests with no sleeps to see how many requests can be made before being rate limited
	- try a short fixed sleep to see if it has made a difference
	- try a variable/randomized sleep 
	- does processing posts from the same instagram profile work better than no processing order?
### Tailscale Optimization
- sudo ethtool -K ppp0 rx-udp-gro-forwarding on rx-gro-list off
	- ppp0 is the network interface
	- ethtool does not persist after reboot
- use networkd-dispatcher
```shell
printf '#!/bin/sh\n\nethtool -K %s rx-udp-gro-forwarding on rx-gro-list off \n' "$(ip route show 0/0 | cut -f5 -d" ")" | sudo tee /etc/networkd-dispatcher/routable.d/50-tailscale sudo chmod 755 /etc/networkd-dispatcher/routable.d/50-tailscale

sudo /etc/networkd-dispatcher/routable.d/50-tailscale test $? -eq 0 || echo 'An error occurred.'
```

## ML Inference server
- microbatching
- bentoml
## FastAPI
> fastAPI is an ASGIWeb framework not a server. uvicorn is the server that will use the API you build to serve requests
- separate services 
	- redis 
	- api integration client
	- parsing client
- cache settings so it's not instantiated every time
### Dependency Injection (DI)
#### When is it not appropriate to use dependency injection pattern
https://softwareengineering.stackexchange.com/questions/135971/when-is-it-not-appropriate-to-use-the-dependency-injection-pattern
#### Why Passing Dependencies to Celery Tasks is Considered Bad Practice: (Chatgpt)

1. **Celery Tasks are Serialized**: Celery tasks are typically serialized and sent to workers. Passing complex objects like database connections or instantiated services can cause issues since these objects might not serialize well or at all.
    
2. **State Management**:
-> What this implies is to create the db session inside the celery task and not to pass the connection as a dependency
### FastAPI Lifespan
- Instantiate connection pools to be shared throughout the lifespan of the app
- Close the connection pool after the app shuts down
### Redis
- connections should be pooled to manage load on the server
- redis connection pool pattern
- redis exponential retry when request fails
- how should services be instantiated? how do they live on the server
- use **Application Factory Pattern**
I've worked mostly on web applications for the last several years. Previously it was Flask, lately it has been FastAPI. The approach that I have found to work best has been to use an [application factory pattern](https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/) and make my connections pools (SQL, Redis, whatever) scoped to the application and configured in the app factory. If you're using Flask, this is the natural pattern that you get pushed into if you're using extensions (ex. Flask-sqlalchemy) to configure and manage your connection pools. With FastAPI (this should also work with starlette), I'll create subnamespaces under `app.state` for my connection pools. So, I can do things like `with request.app.state.db.session_factory() as session: ...`. In FastAPI, I'll wrap this up in a function and use it in my endpoint declaration like `session: db.Session = fastapi.Depends(db.get_session)` (I think litestar offers something similar), but I understand that starlette doesn't implement this paradigm.

This approach has worked well for me. It makes it easy to configure or mock connection pools at runtime during tests, so it's easy to replace `redis` with `fake-redis` or stand-up a test session scoped postgres database with `testing.postgres`, which means you don't need to write config files / env variables telling how to access the database server for testing. It also makes it easy to run tests concurrently, and it helps avoid problems of state "leaking" between tests.

### Using `__main__.py` instead of `main.py`
- instead of python main.py, the app is wrapped inside a module.
- run the app by calling the module name `python -m intrend`

### RabbitMQ vs Redis as a Message Broker
https://cloudinfrastructureservices.co.uk/rabbitmq-vs-redis-message-brokers/

### RabbitMQ as message broker + Celery as task queue + Redis as results backend
- rabbitmq manages its own queues and stores messages internally (either in memory or on disk). It doesn't rely on external databases for storage
- in complex architectures (ie: distributed systems): redis can be used to cache intermediate results, track job progress, or store outputs
- Redis can be used as a results backend for celery to store job states/results
	- **Asynchronous Processing:** Storing results in Redis allows tasks to be processed asynchronously. Clients can submit tasks and continue with other operations without waiting for the task to complete. They can check back later to retrieve the result.
#### Results backend on redis
- key: user_id
- val: last updated timestamp
### When to batch process
- Reduced network traffic (when communicating with database)
- Atomic Operations: Batching can make error handling simpler by allowing you to treat a batch as a single unit of work. If an error occurs, you can roll back the entire batch rather than dealing with individual task errors.
### Batch Use Case
- Batch all user timeline media into 1 task from rabbitmq
#### Task Producer Logic (RabbitMQ)

```json
{
    "batch_id": "ig_user_id",
    "task_data": "some_data"
}
```

#### Task Consumer Logic (Celery Worker)
- Can also let worker do prefetching
- 
```python
from celery import Celery
import redis

app = Celery('batching_example', broker='pyamqp://guest@localhost//')

r = redis.Redis()

@app.task
def process_batch(batch_id):
    # Fetch tasks for this batch from Redis
    tasks = r.lrange(f'batch:{batch_id}', 0, -1)
    process_tasks(tasks)
    # Remove the batch from Redis after processing
    r.delete(f'batch:{batch_id}')

def process_tasks(tasks):
    # Custom logic to process the batched tasks
    print(f"Processing batch with {len(tasks)} tasks")

@app.task(bind=True)
def collect_task(self, batch_id, task_data):
    # Add the task to the batch in Redis
    r.rpush(f'batch:{batch_id}', task_data)

    # Example condition: process the batch if it has 10 tasks
    if r.llen(f'batch:{batch_id}') >= 10:
        process_batch.delay(batch_id)
```
![fastapi and celery queue user flow](https://testdriven.io/static/images/blog/fastapi/fastapi-celery/fastapi-celery-flow.png)
### Ensuring Operations in Celery
In Celery; If a task takes 10 minutes to complete, and there are 10 new tasks coming in every minute, the queue will never be empty. This is why it’s very important that you monitor queue lengths!

A way to do this is by [using Munin](https://docs.celeryq.dev/en/stable/userguide/monitoring.html#monitoring-munin). You should set up alerts, that’ll notify you as soon as any queue has reached an unacceptable size. This way you can take appropriate action like adding new worker nodes, or revoking unnecessary tasks.
### De-normalized Data Warehouse
  
Both transactional data and data warehouses can be hosted in an RDBMS, with traditional tables and relationships. If both are tables and relationships, why do we need to store data twice?

The answer is that transactional databases are designed for efficient updates, and tables are normalized. Reporting on such databases is possible, but not efficient. A data warehouse on the other hand is designed for efficient reporting and analysis, and tables are de-normalized for fast query. The downside of this organization is that it is not easy to update data. Because of de-normalization, the same data is often stored in multiple places, so maintaining consistency while updating is very hard.

That means if data has changed since the last time the data warehouse was built -- and those changes are important to incorporate -- it is usually easier to tear down the old data warehouse and rebuild it.
- Useful for storing preprocessed data for machine learning 
### DB Connection Pools
- Should be a singleton so it is not instantiated upon every request

### Transient Queues
Queues created by Celery are persistent by default. This means that the broker will write messages to disk to ensure that the tasks will be executed even if the broker is restarted.

But in some cases it’s fine that the message is lost, so not all tasks require durability. You can create a _transient_ queue for these tasks to improve performance:

### Job Queue
- Jobs should be recorded in a persistent store (relational DB) with a status
- Every job that gets added to the queue, there should be a worker that updates the job record
- In the event of a redis instance restart/crash, you need a worker to hydrate the queue for jobs that weren't picked up yet (ie: if older than a threshold)
### Asynchronous vs Synchronous Tasks



### Extracting the data
- accept encoded data (zstd) to reduce network bandwidth and storage
- decompress -> bytes
- decode bytes to utf-8
- load into json and parse with jmsepath
### Figuring out the IG rate limiter
- limited when extracting too many profiles does not limit extracting posts
- there can be 401 error when extracting a page
- even after receiving  Response content: {"message":"Please wait a f
ew minutes before you try again.","require_login":true,"status":"fail"}, I can continue extracting pages

### Middleware
Middleware is a general term for functions / software that live inside (in the middle) of a request / response cycle and usually have access to the request object. It's for things like auth, error logging, parsing, etc.

A very simplified version to illustrate would be something like:

```python
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

### Logging Metrics with Grafana and Prometheus
https://dev.to/ken_mwaura1/getting-started-monitoring-a-fastapi-app-with-grafana-and-prometheus-a-step-by-step-guide-3fbn
## Setting up 4G modem
- mmcli can rotate ip instantly by enabling and disabling modem
- To delete apn in ubuntu, use nm-connection-editor
- ip is unable to rotate after disabling and enabling sometimes
	- this might be a bug in mmcli
	- in mmcli --debug mode, it's seen that bearer profile -1 is somehow activated but unable to be deactivated
- one way to solve this is to power cycle the usb, not possible to do in ubuntu without usb hub that has power cycling functionality

### Switching to Huawei Modem
- possibly switch to e3372h which has better hilink router interface 
### How are ip addresses assigned?
- dynamically assigned by carrier
- switching bands or apn does not switch you to a different block
- telus range: 209.29.168.0/16 is common, 209.29.99.0/16 is not often seen

## Production Web Server Components

### gunicorn (Middleware)
gunicorn is [Green Unicorn,](https://gunicorn.org/) it acts as an interface between a production web server like nginx and your flask application.

WSGI is a web server gateway interface (a specification only used in python ecosystems),that define how web servers and appications interact. the technology that gunicorn implements.

WSGI is a spec that standardizes a way for traditional web servers (nginx, apache, etc) communicate with web applications and frameworks like flask. Traditional web servers don't understand how to communicate directly with web applications like flask so you need something to sit in the middle, which is where a WSGI server comes into play. Gunicorn is an implementation of a WSGI server that will act as the intermediary between a tradition web server and your flask application. While you could server out your app with just the wsgi server, it is more common to situate it behind a web server (nginx > gunicorn > flask app code).
- each process has it's own memory
- ie: each process has it's own fastapi app, celery app, connection pool
- make sure that the total connections allowed (sum of all workers' connection pools) does not exceed maximum connections allowed to the database
### Uvicorn
- ASGI
- Uvicorn is a web server. It handles network communication - receiving requests from client applications such as users’ browsers and sending responses to them. It communicates with FastAPI using the [Asynchronous Server Gateway Interface (ASGI)](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface), a standard API for Python web servers that run asynchronous code. This leaves FastAPI and our application code free to concentrate on the HTTP layer and application logic, without worrying about the low-level details of network connections.
- gunicorn is usually used in conjunction with uvicorn
- allows asynchronous workers: useful for fastapi
### Optimal Number of Uvicorn Workers needed in Production
https://sentry.io/answers/number-of-uvicorn-workers-needed-in-production/
- number of workers = number of cores * number of threads + 1 
## Why RabbitMQ?
[What is a message broker?](https://www.ibm.com/cloud/learn/message-brokers)
[Can someone explain what message brokers are used for?](https://stackoverflow.com/questions/730364/can-someone-explain-what-message-brokers-are-used-for)
It's an implementation of the [pub-sub pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern) and for when you want to do things like load balancing. You put a bunch of jobs in queue and they get distributed to a number of workers.

This is most useful for when you're running a highly scalable application in the cloud and part of your solution to dealing with increased traffic (or work) is to spin up more instances of the app and distribute the load across multiple servers. Each instance picks a message off the queue, which represents some work it has to do, does it and moves on to the next. Software like RabbitMQ deals with the headache of deciding how to distribute the work to the workers.

An example would be posting a Reddit comment. It goes into a queue and is eventually handed to a worker. It takes my request, does some validation, cleanup etc. and dumps it in a database somewhere. If people post too many comments at once and they can't keep up, more workers get spawned (usually) automatically. All of the large websites, games or apps with 500k+ users are using message brokers in one capacity or another. At that scale you have to distribute the work. There's no choice.
## RabbitMQ
- Message queues should never contain data, only actions telling it what to do
	- ie: poll database, process some data, etc
- You have to assume the messages will be lost unless you are using a persistent message queue.
- If you are using a persistent message queue, well that's just a database with a funny name.
### How it will be used in my project
- API extraction queue
- Media processing/downloading queue
- LLM batch processing queue
- Frontend Queue?
	- For example: when stats get updated, I want it to update realtime for users
	- **Can be used to get real-time count of # of hashtags**
### Polling Architecture
- Hydrating the the message queue


### Rabbitmq on MAC
```zsh
brew services start/stop/restart rabbitmq
```

- web-api exists at port 15672 while the actual port it communicates with other apps is 5672
### Celery Queues
- queues created by rabbitmq are persistent even after restart
- they have to be explicitly deleted
## Celery
### Async in Sync Tasks
https://stackoverflow.com/questions/70960234/how-to-use-asyncio-and-aioredis-lock-inside-celery-tasks

### [Async url requests in celery](https://stackoverflow.com/posts/24639070/timeline)

Requests don't have to made asynchronously because Celery is already made to execute jobs asynchronously. Adding async url call in an async task would be unnecessary overhead 
### Task_always_eager
https://stackoverflow.com/questions/45353574/how-to-spawn-a-celery-task-from-previous-celery-task
### Celery App
- Should be a stand-alone deployment and not inside fastapi
- better resource management
### Celery App Factory
https://testdriven.io/courses/flask-celery/app-factory/

### Multiple Workers
- --without-gossip:	https://stackoverflow.com/questions/21132240/celery-missed-heartbeat-on-node-lost
- Each worker has to be named `-n worker2@host`

### Celery General
- Always pass object refs by ID and have the task pull directly from the db and your broker will get you much further.

```python
# Send Message
@app.task(bind=True)
def hello(self, a, b):
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 50})
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 90})
    time.sleep(1)
    return 'hello world: %i' % (a+b)

def on_raw_message(body):
    print(body)

a, b = 1, 1
r = hello.apply_async(args=(a, b))
print(r.get(on_message=on_raw_message, propagate=False))


# Retry policy
add.apply_async((2, 2), retry=True, retry_policy={
    'max_retries': 3,
    'interval_start': 0,
    'interval_step': 0.2,
    'interval_max': 0.2,
    'retry_errors': None,
})

retry_backoff=True

# Operational Error: message transport conn lost, or conn can't be initiated
# Raised only after retries are exhausted
try:
		add.delay(2,2)
except add.OperationalError as exc:
     logger.exception('Sending task raised: %r', exc)
```

### Compress Messages
```python
add.apply_async((2, 2), compression='zlib')
```

### Always write idempotent tasks
> task shouldn't cause unintended effects even if called multiple times with the same arguments, can occur in distributed setups
https://gplhegde.hashnode.dev/using-celery-in-django-production-setup#heading-always-write-idempotent-tasks
- use database lock

### Handling Task Failures
- exponential backoff while retrying
### Worker pool configuration
- By default, each task is executed in a separate thread by the Celery worker. As you know, threads have their own stack, they turn out to be a bit expensive for certain types of tasks that are purely I/O bound.
- Generally, it is a good idea to separate your I/O-bound and CPU-bound tasks into different queues and run separate celery worker processes with appropriate worker pool configurations for these queues.
- io-bound, user gevents or eventlet pool with high concurrency factor: `celery worker --app=example --pool=gevent --concurrency=100` 
- cpu bound: default prefork pool with default concurrency: `celery worker --app=example --loglevel=info
`
- more on execution pools: https://celery.school/celery-worker-pools
### Avoid shared global variables

Remember that each task is executed in its own thread and tasks are executed in parallel by the worker process. It is a bad idea to use global variables that are read and written by the tasks.

In the event that global variables cannot be avoided, access them with a distributed lock.
### Ignore unnecessary task results
```python
from celery import shared_task

# by default all runs of this task ignore the result
@shared_task(ignore_result=True)
def sample_task():
    pass

# result will be stored and returned
result = sample_task.apply_async(ignore_result=False).get(timeout=30)
```


### Celery Worker Prefetch Limits
- The prefetch limit is a **limit** for the # of tasks a worker can reserve for itself
- If prefetch is 0, the worker will keep consuming messages not respecting it's memory limit or that there may be other available worker nodes that may be process them sooner
- The workers default prefetch count is the **worker_prefetch_multiplier** setting multiplied by the number of concurrency slots (process/threads/green-threads)
	- This doesn't apply to rabbitmq and other brokers that deliver messages round-robin
- If you have tasks with a long duration, you want the multiplier to be one, meaning it'll only reserve one task per worker process at a time
- If you have many short-running tasks and throughput/round trip latency is important, this number should be large
	- Experimenting is required to find the best value 

### How Celery Works
- _Celery_ is _workers_ pulling jobs from a queue.
- when starting a celery worker, it must be able to find the app (an instance of Celery()) in the specified module
In short Celery uses a set of terms that are useful to understand when building a system of distributed work.

- Client: FastAPI - A "client" is any code that runs celery tasks asynchronously.
- Worker: Celery Worker- An application that gets the work done: 
- Broker: RabbitMQ - The means by which Client asks Worker to do work.
- Application - An instance of the Celery class

Every component can be on a different server

It should be no surprise then, that the application typically has the Broker configured with a URL. That is all the Applications, in all the Clients and Workers are all using the same Broker URL and hence are all using the same Broker.

Web and worker nodes are essentially plain servers, with a key distinction: Web nodes handle incoming requests from the internet and dispatch jobs for asynchronous processing, while Workers are the machines responsible for picking up these tasks, executing them, and delivering responses.

### Error Tracking with Sentry
- define an abstract base class with on_failure_handler
- log only the exception after max_retries


### Celery app does not need to be in fastapi.main.py
https://towardsdatascience.com/deploying-ml-models-in-production-with-fastapi-and-celery-7063e539a5db
### Concurrency

#### Prefork
```zsh
celery worker -A tasks --loglevel=info --concurrency 5
```

- Most suitable for CPU bound tasks
- the default pool used is prefork (meaning each celery worker gets its only)
- A celery worker that controls 5 processes. The worker distributes tasks among the 5 processes.
- Each process is independent with its own separate memory space. No direct memory is shared between processes
- The prefork pool implementation is based on Python's multiprocessing package. It allows your Celery worker to side-step Python's Global Interpreter Lock and fully leverage multiple processors on a given machine.
#### Thread Pool + Gevent
- Multithreading with the same process (shared memory between threads)

#### Some Caveats on Concurrency
- Although I/O bound tasks are more suited for multithreading, sqlalchemy + asyncio + celery don't play well (some problem about not returning to the same event thread + sharing sessions is a no go with sqlalchemy), the best option here is multi processing (prefork or multiple workers)

### Avoid launching synchronous subtasks[¶](https://docs.celeryq.dev/en/latest/userguide/tasks.html#avoid-launching-synchronous-subtasks "Link to this heading")
```python
@app.task()
def fetch_page(url):
    return myhttplib.get(url)

@app.task()
def parse_page(page):
    return myparser.parse_document(page)

@app.task(ignore_result=True)
def store_page_info(info, url):
    PageInfo.objects.create(url=url, info=info)
------------------------------------------------
# Bad
@app.task
def update_page_info(url):
    page = fetch_page.delay(url).get()
    info = parse_page.delay(page).get()
    store_page_info.delay(url, info)

# Good
def update_page_info(url):
    # fetch_page -> parse_page -> store_page
    chain = fetch_page.s(url) | parse_page.s() | store_page_info.s(url)
    chain()
```
### [Performance and Strategies](https://docs.celeryq.dev/en/latest/userguide/tasks.html#id17)[](https://docs.celeryq.dev/en/latest/userguide/tasks.html#performance-and-strategies "Link to this heading")

### Granularity[](https://docs.celeryq.dev/en/latest/userguide/tasks.html#granularity "Link to this heading")

The task granularity is the amount of computation needed by each subtask. In general it is better to split the problem up into many small tasks rather than have a few long running tasks.

With smaller tasks you can process more tasks in parallel and the tasks won’t run long enough to block the worker from processing other waiting tasks.

However, executing a task does have overhead. A message needs to be sent, data may not be local, etc. So if the tasks are too fine-grained the overhead added probably removes any benefit.

See also

The book [Art of Concurrency](http://oreilly.com/catalog/9780596521547) has a section dedicated to the topic of task granularity [[AOC1]](https://docs.celeryq.dev/en/latest/userguide/tasks.html#aoc1).
### SQLAlchemy
http://www.prschmid.com/2013/04/using-sqlalchemy-with-celery-tasks.html
### Database transactions[](https://docs.celeryq.dev/en/latest/userguide/tasks.html#database-transactions "Link to this heading")

Let’s have a look at another example:

```python
from django.db import transaction
from django.http import HttpResponseRedirect

@transaction.atomic
def create_article(request):
    article = Article.objects.create()
    expand_abbreviations.delay(article.pk)
    return HttpResponseRedirect('/articles/')
```
This is a Django view creating an article object in the database, then passing the primary key to a task. It uses the transaction.atomic decorator, that will commit the transaction when the view returns, or roll back if the view raises an exception.

There’s a race condition if the task starts executing before the transaction has been committed; The database object doesn’t exist yet!

The solution is to use the `on_commit` callback to launch your Celery task once all transactions have been committed successfully.
```python
from django.db import transaction
from django.http import HttpResponseRedirect

@transaction.atomic
def create_article(request):
    article = Article.objects.create()
    transaction.on_commit(lambda: expand_abbreviations.delay(article.pk))
    return HttpResponseRedirect('/articles/')
```

### Pickleable Exceptions
### Creating pickleable exceptions[](https://docs.celeryq.dev/en/latest/userguide/tasks.html#creating-pickleable-exceptions "Link to this heading")

A rarely known Python fact is that exceptions must conform to some simple rules to support being serialized by the pickle module.

Tasks that raise exceptions that aren’t pickleable won’t work properly when Pickle is used as the serializer.

To make sure that your exceptions are pickleable the exception _MUST_ provide the original arguments it was instantiated with in its `.args` attribute. The simplest way to ensure this is to have the exception call `Exception.__init__`.

Let’s look at some examples that work, and one that doesn’t:
```python

# OK:
class HttpError(Exception):
    pass

# BAD:
class HttpError(Exception):

    def __init__(self, status_code):
        self.status_code = status_code

# OK:
class HttpError(Exception):

    def __init__(self, status_code):
        self.status_code = status_code
        Exception.__init__(self, status_code)  # <-- REQUIRED

```

So the rule is: For any exception that supports custom arguments `*args`, `Exception.__init__(self, *args)` must be used.

There’s no special support for _keyword arguments_, so if you want to preserve keyword arguments when the exception is unpickled you have to pass them as regular args:

```python
class HttpError(Exception):

    def __init__(self, status_code, headers=None, body=None):
        self.status_code = status_code
        self.headers = headers
        self.body = body

        super(HttpError, self).__init__(status_code, headers, body)
```

### Task  handlers
- before_start
- after_return
- on_failure
- on_retry
- on_success
### Ignore results you don’t want[](https://docs.celeryq.dev/en/latest/userguide/tasks.html#ignore-results-you-don-t-want "Link to this heading")

If you don’t care about the results of a task, be sure to set the [`ignore_result`](https://docs.celeryq.dev/en/latest/reference/celery.app.task.html#celery.app.task.Task.ignore_result "celery.app.task.Task.ignore_result") option, as storing results wastes time and resources.
```python
@app.task(ignore_result=True)
def mytask():
    something()
# or per execution basis
result = mytask.apply_async((1, 2), ignore_result=False)
```

### How to use a celery task inside a route
- Import the celery task
- `task.dummy_task.delay()`, delay is equivalent to `.apply_async()`
### Purging Queues
```zsh
celery -A intrend.services.celery_worker.celery_app purge
celery -A APP_NAME purge --queues QUEUE_NAME
```

### Starting Celery Worker
```python
celery -A intrend.services.celery_worker.celery_app worker --loglevel=info --concurrency=1
celery -A intrend.services.celery_worker.celery_app flower --port=5555
```

### Autoreload in dev

```zsh
pip install watchdog
watchmedo auto-restart --directory=./intrend/services/celery_worker/ --pattern=*tasks.py --recursive -- celery -A intrend.services.celery_worker.celery_app worker --concurrency=1 --loglevel=INFO

```
  
### Celery Config
- settings file with environment variables prefixed by a namespace such as 'CELERY'
### Including Tasks
- 
### Flower Monitoring


### Remote Celery Worker
1. **Django app**: Celery tasks are defined here. It has Celery installed as dependency.
    
2. **Message broker**: A message broker gets this task from 1. and queues it.
    
3. **Celery Worker**: This is actually not a separate python app that only contains Celery. It is a _full blown instance of 1._. So you launch Django _twice_, one is producing tasks and the other is working on them. Both containing the same `@shared_task` function.
    
- If you update your main Django app and not restart Celery worker, your workers are working on a stale version of the `@shared_task` function.
- The app in 1. is launched using Gunicorn (or whatever you want), but App in 3. is launched using `celery -A "your_app" workers -l INFO`. It's not running Gunicorn, but still contains all the code in 1.
- Configure celery workers on the django app to listen to only specific tasks
- The celery worker on the separate server will be used to listen to messages from the broker and store processed results on redis
- The web server than pulls results from redis
### Routers
Celery on Server A can still route tasks to `server_b_queue` even if it doesn't have a worker that listens to `server_b_queue`
- tasks are first sent to rabbitmq
```python
# Automatic Routing
task_routes = {'feed.tasks.import_feed': {'queue': 'feeds'}}
celery -A proj worker -Q feeds

# Manual Routing
def route_task(name, args, kwargs, options, task=None, **kw):
        if name == 'myapp.tasks.compress_video':
            return {'exchange': 'video',
                    'exchange_type': 'topic',
                    'routing_key': 'video.compress'}
task_routes = (route_task,)
task_routes = ('myapp.routers.route_task',)
Excluding Queues

```
#### Excluding Queues
By default celery worker will read from all queues. You can exclude queues that a worker listens to with
```bash
celery -A proj worker -l INFO -X feeds
```

### Shared Task
https://appliku.com/post/celery-shared_task/#:~:text=The%20%22shared_task%22%20decorator%20allows%20creation,import%20the%20Celery%20app%20instance.
The "shared_task" decorator **allows creation of Celery tasks for reusable apps as it doesn't need the instance of the Celery app**. It is also easier way to define a task as you don't need to import the Celery app instance.

#### Circular Imports
If you are `task.delay()` from `models.py` and `tasks.py` is importing anything from models – you will get a circular import error and tasks will not get initialized. Also if you are sending task from a totally different app, working with the same Celery instance – you can't use `import` and thus can't do `.delay` or `.apply_async`

### Progress Bar
https://celery.school/celery-progress-bars-with-fastapi-htmx
## DB

### Creating Database
#### What is `template1`?

- **Template Database**: `template1` is one of the system databases in PostgreSQL that serves as a template for creating new databases. When you run the `CREATE DATABASE` command, PostgreSQL copies the contents of `template1` to the new database.
    
- **System Database**: It is a system database that comes pre-configured with PostgreSQL. It contains the default schema and objects that are copied to new databases.
#### Creating Tables 
- You need to ensure that all models/tables that are defined in your application are imported before running create_all. If a module is not imported its table is not registered in the metadata, so sqlalchemy cannot create it.
```python
await conn.run_sync(Base.metadata.create_all)
```
### Alembic


https://dev.to/r0mymendez/simplify-database-migrations-using-python-with-alembic-4bhd

### Avoiding Race Conditions with SQLAlchemy
https://dev.to/ivankwongtszfung/safe-update-operation-in-postgresql-using-sqlalchemy-3ela

### Database Provisioning

ORM: SQLAlchemy
Migrations: Alembic

### Calculate timestamps within your DB, not your client
For sanity, you probably want to have all `datetimes` calculated by your DB server, rather than the application server. Calculating the timestamp in the application can lead to problems because network latency is variable, clients experience slightly different clock drift, and different programming languages occasionally calculate time slightly differently.
https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime

### SQLAlchemy + Celery
https://celery.school/sqlalchemy-session-celery-tasks?source=more_articles_bottom_blogs

### SQLAlchemy
- Column vs Mapped_column
	- mapped_column: supports direct typing in python
	- `col: Mapped[str] = mapped_column(unique=True)`
### Creating Schemas


### Commit and Flush
https://stackoverflow.com/questions/4201455/sqlalchemy-whats-the-difference-between-flush-and-commit
- session object = ongoing transaction of changes to database
- operations arent persisted to db until commit
- flush communicates a series of operations to the db
- flush is always calledAs part of a call to commit

## Concurrency vs Parallelism
> Ability to handle multiple operations at the same time

- Concurrency: A condition that exists when at least two threads are making progress. A more generalized form of parallelism that can include time-slicing as a form of virtual parallelism.
- Parallelism: A condition that arises when at least two threads are executing simultaneously
### Multi-threading (Concurrency)
### Asynchronous

### Multi-processing (Parallelism)






## Tailscale

```shell
tailscale up --accept-dns --advertise-connector --advertise-tags=tag:proxy --advertise-routes=.../24
```
- something weird might be going on when advertising routes before advertising connectors
- app connector may be overwritten...
- do a --reset, advertise connectors first and then do
```shell
tailscale set --advertise-routes ...0/24
```

## Docker
### It is possible to limit Resources on a multi-container application

## Self Hosting
What I do:
1. Use Cloudflared (Cloudflare Tunnel) to get into my host computer, instead of port forwarding
    
2. Use an NGINX proxy in front of all my applications (even if there's only one).
    
3. Install CrowdSec, with the NGINX bouncer and parser, which will block (and detect) malicious actors.
    
4. If possible, set up a firewall in your router blocking your host computer from being able to reach anything else on your network (look up DMZ network).

If you _do_ insist on hosting it from a pi on your network, look into DMZ (de-militarized zone) in your router settings. putting the pi into the DMZ will help protect the rest of your systems in the event the pi is compromised. although you will need to verify if the dmz setting on your router is actually separate or not - try to connect from the pi to other hosts and see if it is truly isolated or not.



# Rust
## Concurrency
https://jeehoonkang.github.io/2017/08/23/synchronization-patterns.html
https://www.reddit.com/r/rust/comments/1ca2cu9/learning_concurrency_in_rust/
rust atomics nad locks

**  
First steps**

See [https://www.rust-lang.org/learn](https://www.rust-lang.org/learn)

- Read _the bock_ [https://doc.rust-lang.org/book/](https://doc.rust-lang.org/book/)
    
- Do the [https://github.com/rust-lang/rustlings/](https://github.com/rust-lang/rustlings/) course
    
- Check out [https://doc.rust-lang.org/rust-by-example/](https://doc.rust-lang.org/rust-by-example/)
    

Stay up-to-date by subscribing to the newsletter [https://this-week-in-rust.org/](https://this-week-in-rust.org/)

**Grow**

- Read the practical guide [Programming Rust, 2nd Edition](https://www.oreilly.com/library/view/programming-rust-2nd/9781492052586/). Experienced systems programmers will learn how to successfully bridge the gap between performance and safety using Rust.
    
- Read [Rust Atomics and Locks](https://marabos.nl/atomics/) by Mara Bos to gain a clear understanding of low-level concurrency. You’ll learn everything about atomics and memory ordering and how they’re combined with basic operating system APIs to build common primitives like mutexes and condition variables.
    
- [Rust for Rustaceans](https://rust-for-rustaceans.com/) by Jon Gjengset covers everything you need to build and maintain larger code bases, write powerful and flexible applications and libraries, and confidently expand the scope and complexity.



# Misc
## Protecting private keys in the cloud
https://www.linkedin.com/pulse/protecting-private-keys-cloud-raz-halaly



# IG API

Error: 'URL signature expire'
Instagram CDN URLs contain timestamp components that allow them to expire after a while



# Elasticsearch

### . **Building Dashboards with Kibana**

- **Kibana** (part of the Elastic Stack) is a powerful tool for visualizing trends:
    - **Line Charts**: Plot keyword frequency or overall caption volume over time.
    - **Word Clouds**: Visualize the most frequent keywords in the captions over specific time periods.
    - **Bar Charts & Pie Charts**: Display breakdowns of caption types, keywords, or other categories.
    - **Time-series Analysis**: Create dashboards that show how certain keywords, phrases, or sentiments evolve over time.

### Example Use Cases for Trend Analysis:

- **Identify Seasonal Trends**: If certain words or phrases (e.g., "summer," "holiday") peak at certain times of the year, you can use Elasticsearch to track these seasonal trends.
- **Event-based Trends**: Analyze how captions mentioning specific events (e.g., sporting events, concerts) fluctuate over time.
- **Emerging Topics**: Identify new keywords or topics gaining popularity over a specific time range.
- **Sentiment Shifts**: Track how sentiment in the captions shifts during different time periods or around specific events.

