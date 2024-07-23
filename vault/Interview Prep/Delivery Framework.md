# Delivery Framework 
>Structural approach to delivering a working system

Source: https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery#infrastructure-design-structure

## Requirements (~5 mins)
Functional requirements and Identify top 3-5 most relevant non-functional requirements

1. **CAP Theorem**: Should your system prioritize consistency or availability? Note, partition tolerance is a given in distributed systems.
    
2. **Environment Constraints**: Are there any constraints on the environment in which your system will run? For example, are you running on a mobile device with limited battery life? Running on devices with limited memory or limited bandwidth (e.g. streaming video on 3G)?
    
3. **Scalability**: Types of scaling requirements:
	- Bursty traffic at a specific time of day or during events 
	- Read-write ratio: Does your system need to scale reads or writes more?
    
4. **Latency**: How quickly does the system need to respond to user requests? 
	- Specifically consider any requests that require meaningful computation. For example, low latency search when designing Yelp. 
    
5. **Durability**: How important is it that the data in your system is not lost? For example, a social network might be able to tolerate some data loss, but a banking system cannot.
    
6. **Security**: How secure does the system need to be? Consider data protection, access control, and compliance with regulations.
    
7. **Fault Tolerance**: How well does the system need to handle failures? Consider redundancy, failover, and recovery mechanisms.
    
8. **Compliance**: Are there legal or regulatory requirements the system needs to meet? Consider industry standards, data protection laws, and other regulations.
