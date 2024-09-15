## Browser links 
https://www.instagram.com/explore/tags/cat/
https://www.instagram.com/nala_cat/?hl=en


## Design Considerations
- I opted for JS over Python for a few reasons. Crawlee, the scraping and browser automation library provides proxy management, generation of browser-like headers, and  replication of TLS fingerprints is not yet fully ported to Python.
- The python port currently lacks TLS fingerprints which is important to bypass bot detection while scraping
### Crawlee
- headless browser 
- auomatic retries on errors
- integrated proxy rotation and session management
- configurable request routing 
- persistent queue for URLS
- pluggable storage for data and files
- robust error handling

- block login requests


snapshots to debug


### https certificates
Assuming that the app is using HTTPS to communicate with the server, you'll need extra steps.

Besides encryption, HTTPS also has a mechanism to ensure that you're talking to the server that you think you are. Otherwise, it would be easy for a network operator to engineer a man-in-the-middle attack, where the network operator could watch all traffic you send to, say, your bank.

When you start talking to a server over HTTPS, the server sends back a certificate. This certificate includes both the hostname of the server you're contacting (e.g. secure.example.com) as well as information establishing a chain of trust back to a root certificate authority. I'm not going to go too deep into the details, but you can't forge that chain of trust. Your device includes a list of pre-approved root CAs. As long as there's a chain of trust from the website's certificate to one of those pre-approved root CAs, then the HTTPS request is allowed to proceed.

But like I said, you can't forge those certificates, so how does Postman work? IIRC, at least on Windows, Postman installs an additional root CA certificate in your computer's root CA store. Essentially, it configures your computer to trust one more root CA (Postman itself). It then issues a certificate for e.g. secure.example.com but signed by its own root CA. Your computer sees that the root CA is trusted and allows the request to proceed.

In order to do the same with your iPhone, you'd need to install Postman's root CA certificate onto your phone. IIRC each installation of Postman generates a unique root certificate, so you'll need to install the one from the machine running Postman. I don't have an iPhone so I don't know how you'd do that or if it's even possible.



Instagram uses SSL Pinning. You need to get past that. You can write a small frida script or find countless of them online. 

as far as i know, you can use android emulator, burp suite, [frida](https://github.com/frida/frida) and [objection](https://github.com/sensepost/objection)o

https://www.alexschnabl.com/blog/articles/using-proxyman-to-reverse-engineer-the-instagram-private-api

## emulators
will probably bet banned

## real mobile environment with app cloner

## proxies

### 4g proxy
Login to the router admin page (https://192.168.8.1 in my case) and disconnect+connect (can be automated with a little scripting). 4g connectivity gives you a brand new IP address every time you reconnect.


## Making IG accounts

## PROBLEM WITH MOBILE PROXIES

BAD CONNECTION


## Crawler
- enqueue all new posts and download the images 
