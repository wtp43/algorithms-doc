## Current Solution
- mobile data too expensive in canada
- unlimited 5g data without throttle is possible in the US for a cheap $60
- in the meantime, we'll work with unlimited bandwidth datacenter/residential ip proxies


## Scaling
- use a combination of proxy providers and mobile proxy

## Proxy Providers (Unlimited bandwidth)
> check blackhat for discounts
- stormproxies
	- speed is quite slow
	- connections are limited
	- async needs to be tried
	- ip's are not great quality, frequently get 302


## Mobile Proxies
- rutm50 works good
- to save on data/bandwidth -> speed, route only ig requests through mobile interface
- route all other tailscale traffic through wan/ethernet via ip rules/tables
