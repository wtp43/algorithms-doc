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
 - 