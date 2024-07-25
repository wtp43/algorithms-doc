# Web Crawler

## Functional Requirements 
(Out of scope for interview)
- Handling of non-text data
- Handling of dynamic content (javascript-rendered pages)
- Handling of authentication (login-required pages)

## Non-Functional Requirements 

>[!tip]
> Delay back-of-envelope (BOE) calculations until they are necessary for solving a specific problem.
>

1. Fault tolerance to handle failures gracefully and resume crawling without losing progress 
2. Politeness to adhere to robots.txt and not overload website servers inappropriately
3. Efficiency to crawl the web in under 5 days
4. Scalability to handle 10B pages

(Out of scope)
- Security to protect system from malicious actors
- Cost to operate system within budget constraints
- Legal compliance

## Set Up

### API or System Interface
**System Interface**
1. **Input**: Seed URLs to start crawling from.
2. **Output**: Text data extracted from web pages.


### Data Flow

1. Take seed URL from frontier and request IP from DNS
    
2. Fetch HTML from external server using IP
    
3. Extract text data from the HTML.
    
4. Store the text data in a database.
    
5. Extract any linked URLs from the web pages and add them to the list of URLs to crawl.
    
6. Repeat steps 1-5 until all URLs have been crawled.


## High-Level Design

1. **Frontier Queue**: The queue of URLs we need to crawl. We will start with a set of seed URLs and add new URLs as we crawl the web. The technology used could be something like Kafka, Redis, or SQS. We'll decide on the technology later.
    
2. **Crawler**: Fetches web pages, extracts text data, and extracts new URLs to add to the frontier queue. In the next section we'll talk about how to scale this component to handle the 10B pages we need to crawl.
    
3. **DNS**: Resolves domain names to IP addresses so that the crawler can fetch the web pages. There are interesting discussions to be had about how to cache DNS lookups, handle DNS failures, and ensure that we are not overloading DNS servers. Again, more on this later.
    
4. **Webpage**: TThe external server that hosts the web pages we are crawling. We'll fetch the HTML from these servers and extract the text data.
    
5. **S3 Text Data**: This is where we'll store the text data we extract from the web pages. We choose S3 as our blob storage because it is highly scalable and durable. It is designed to store large amounts of data cheaply. Other hosted storage solutions like Google Cloud Storage or Azure Blob Storage could also be used.

## Fault Tolerance 
Bad: In Memory Timer
- Very likely fetch won't succeed in just a few more seconds
- Not robust since timer is lost if crawler were to go down
Good: Kafka with Manual Exponential Backoff
- Kafka doesn't support retries, manually implement them 
- Separate 

## Misc

### Finding API Endpoints
-  Scraping is required if the webpage is server side rendered

check for  user agent restrictions, referrer dependencies, and credentialing.