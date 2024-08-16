
## Network Basics

### NAT (Network Address Translation)
- Most mobile networks use NAT, meaning the modem gets a private IP address from the provider, not a public one


### CGNAT 
- Carrier grade NAT does not allow port forwarding as ip is shard between users
### Port
- Communication endpoint used to organize and differentiate traffic
- Web traffic typically uses 80 (http) or 443 (https)

### Port Forwarding 
- Open port on modem to listen for traffic
- ip address = private/internal ip address of the modem
### Tunneling
- Cloudflare Tunnel Client is a tunneling daemon that proxies traffic from the Cloudflare network to your origins
- Useful for when port forwarding is not possible

```shell
cloudflared tunnel login
cloudflared tunnel create <tunnel-name>

# Generate Configuration File
cloudflared tunnel route dns <tunnel-name> <subdomain.yourdomain.com>
```

 Config File
 ```yaml
 tunnel: <tunnel-id> credentials-file: /home/yourusername/.cloudflared/<tunnel-id>.json 

ingress: 
- hostname: proxy.yourdomain.com service: http://localhost:8080 
- service: http_status:404
```
-  cloudflare tunnel will also update the dns if your ip is dynamic
- sudo cloudflared --config /home/username/.cloudflared/config.yml service install
	- Cloudflared may not look in the correct directory 
- sudo systemctl start cloudflared
- sudo systemctl enable cloudflared

## Proxies
- When setting up a proxy server, you can configure it to listen on a specific port
- For a proxy server to be accessible from the internet, it needs to have a public IP
	- Port forwarding from the public IP to the private IP must be configured, generally through Dynamic DNS 


### Setting up DDNS through Cloudflare
- Generate API token
- Add DNS edit permissions for Zone
- Add client IP whitelist
- Define time to live (TTL) of token

