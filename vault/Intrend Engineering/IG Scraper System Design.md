# Project Features 

- https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pad/en   
- hashtag scraping (https://app.brandmentions.com/h/p/821491/%23cat)


## Data Flow

1. Extract seed URL from frontier and request IP from DNS
2. Fetch HTML from external server using IP
3. Store raw html into data lake (AWS S3)

## Table Schemas
### Data lake: S3 buckets

| url | html |
| --- | ---- |
|     |      |

### Data warehouse: PostgresSQL 
#### Sources
- Trend table
	- Textile, color, brand 
- URL's
	- Distinct table per site

| url |     |
| --- | --- |
|     |     |
#### Instagram Metrics
- Hashtag table 
- Media posts 
#### TikTok Metrics

#### Google Trends Metrics


### Metadata DB: Amazon DynamoDB (NoSQL Key-Val DB)

| URL | type?                     | last_crawled          | S3 location |     |     |
| --- | ------------------------- | --------------------- | ----------- | --- | --- |
| ... | ig, tiktok, google trends | -crawl every 24 hours |             |     |     |


## Frontier Queue
I'd recommend using whatever the native messaging service is for your hosting provider. SNS/SQS for AWS, Pub/Sub for GCloud, etc

If your host doesn't have one, use the simplest one you can unless and until you need the features of a more advanced service. I would steer clear of things like RabbitMQ or Kafka unless you really need one of the advanced features they offer. Maintaining and managing them can literally be a devops persons full time job  

### Python Redis Queue
https://python-rq.org/docs/exceptions/
- Queue of URL's needed to be scraped 
- Redis Queue or AWS simple Queue Service 
https://app.redislabs.com/#/add-subscription/essential?dbUseCase=cache 
- free 30mb vps, 30 connections

### Populating Queue
- rq-scheduler
- check last crawl date in nosql
- 

### Monitor Queue
https://github.com/Parallels/rq-dashboard
## Scraper 

![[Pasted image 20240723175120.png]]  


### Fault Tolerance  
#### Resumable Iterator 
- Iterator dumps raw HTML in blob storage to be processed later 
- Update URL metadata 
- Put url id onto parsing queue
- If a scrape fails, it stays in the frontier queue
#### Frontier Queue
- URL stays in queue until it is confirmed to have been fetched by a crawler and the HTMl is stored 
- If a crawler goes down, the URL will be picked up by another crawler
- Retry failed scrapes with redis queue exponential backoff
- To prevent excessive delays, cap exponential backoff at a max value 
- After a certain number of failures, message is moved to a dead-letter queue (DLQ). Message will be considered unprocessable (possibly raise/log some error)
#### Crawler Generation 
>What happens if a crawler goes down?
- spin up anew one 
#### Update URL Status 
- DynamoDB to store URL's that have been fetched and processed 
	- Store link to the blob storage where the HTML is stored
	- Store link to the blob storage where the text data is stored 
	- Why?: it would be an anti-pattern to store raw HTML in the queue itself 
	- Queue message will just be the id of the URL in the metadataDB 
#### Text & URL Extraction
- Single stage done in parallel

### Crawler Design
- Cloudflare blocks requests that aren't`http2`
- Crawlee supports http2 while python requests does not

### Bypassing Bot Detection
#### Mimic Human Behaviour
- random movements
- scrolling
- randomly make errors
- typing
#### Hide Browser fingerprint, Valid Fingerprint Generation
sites can create fingerprint of your browser and block you by checking it. by default browsers aren't really trying to hide many fingerprinting vectors
- use browser that masks fingerprints
- use mobile browser: crawlee for python and playwright
- 

### Session Persistence 
load balancer that supports session persistence to ensure that requests from the same domain are always routed to the same crawler machine.
###  Proxies and DNS 
- Cache DNS lookups, handle DNS failures, ensure we are not overloading DNS servers
- residential proxies vs mobile proxies

## Specifically Scraping


Here's what I learnt, if authentication is important, and a necessary prerequisite, try to use something like a "session" instead of making direct requests, this way, you keep the cookie and any other headers. Also better performance!

When I say sessions, I am referring to the requests.Session class within the python request module. There _has_ to be a javascript or npm equivalent of that.

You probably would have noticed, but subsequent requests after the initial authentication request, would be denied without the presence of relevant cookie/token/some other way they validate sessions.

My approach, initially started with having selenium used to login, and store the session cookies and close the browser, and work with the cookies. I then realised that I did not need a headless browser at all!

After which I used mitmproxy to figure how which api endpoints or some ajax request was being used to actually get the data, I got those, and stored them. I did so manually, but you can use selenium to track the network requests to compile a list of XHR/Fetch requests made, and then check their input requirements.

All in all, I ended up getting data FASTER than the site loaded normally! Because I wasn't downloading unnecessary stuff like images, animated gifs/svgs. It was also more robust to changes as it's not often people change endpoints.


### Extracting Data from HTML
ScrapeGraphAI: https://github.com/ScrapeGraphAI/Scrapegraph-ai 
- Use LLM to scrape 
## Parsing Queue
- Fetch S3 url from MetadataDB 
- Download HTML from S3
- Process text from HTML
- Save processed text to data warehouse
- Optional: Put extracted url's back onto frontier queue

## Scaling Up

### Kubernetes Cluster

## Logging

- Configure rentention times

## Site Monitoring
- Prometheus (time series DB ) is a system to collect and process metrics


## LLM API

 You need to be able to effectively serve inferences to many clients simultaneously that can scale - typically this means serializing your model and then having an inference server that serves the predictions. Then you need an API that exposes this to your clients. There are several solutions for this, such as Triton, vLLM, and Mosec, but there always seems to be some "gotcha" that is pretty frustrating:

1. Triton Inference. This is usually my go-to, as it is extremely reliable and fast. You typically want to serialize your models to ONNX, but huggingface only supports exporting [some models](https://huggingface.co/docs/optimum/exporters/onnx/overview) to ONNX and they are usually older. That said, this may work for you.  
 it seems like you can [export](https://huggingface.co/docs/transformers/torchscript) any huggingface model to torchscript and then load this model into Triton. I haven't done this with generative models, so I am unsure what sort of challenges you might face. This person [talks](https://github.com/vllm-project/vllm/issues/178#issuecomment-1603926703) some about it (comparing triton to vLLM) and links to a larger article. 