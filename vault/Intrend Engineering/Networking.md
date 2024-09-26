
ip route add default via 192.168.1.1 dev wan

# mark packets from tailscale
iptables -t mangle -A PREROUTING -i eth0 -p udp --dport 41641 -j MARK --set-mark 1

# route marked packets to eth0
ip rule add fwmark 1 table 100
ip route add default via <gateway_ip> dev eth0 table 100

# allow eth0 to receive packets with mark '1'
iptables -A INPUT -i eth0 -m mark --mark 1 -j ACCEPT
iptables -A OUTPUT -o eth0 -m mark --mark 1 -j ACCEPT

# drop packets on mobile interface not marked '1'
iptables -A INPUT -i mob1s1a1 -m mark ! --mark 1 -j DROP
iptables -A OUTPUT -o mob1s1a1 -m mark ! --mark 1 -j DROP



ip route add 10.16.28.192/32 via 192.168.1.1/24 dev mob1s1a1


## NAT rules in ip tables
- used to translate ip addresses and ports in packets
- commonly used for masquerading and port forwarding
- **SNAT**: Source Network Address Translation, used to modify the source IP of packets.
- **DNAT**: Destination Network Address Translation, used to modify the destination IP of packets.
- **Masquerading**: A form of SNAT used for dynamically allocated IP addresses.
## iptables
- iptables are used for packet filtering, NAT (network address translations), and mangle operations
- possible routing chains`INPUT`, `OUTPUT`, `FORWARD`, `PREROUTING`, and `POSTROUTING`
- tables are specified in `/etc/iproute2/rt_tables`
## ip rules
- used to control routing decisions based on packet attributes


```sh
# mark packets from tailscale
# -j or --jump specifies what action to take when a packet matches this rule
# prerouting chain applies to packets as they arrive at the router, before the system decides where to route them (internally, to another network interface, or to WAN)

iptables -t mangle -A PREROUTING -i wan -p udp --dport 41641 -j MARK --set-mark 1

# OUTPUT chain: packets destined for a machine outside of the local machine

# INPUT chain: packets destined for a machine inside the local machine

# allow table one interfaces to only accept packets marked with 1
# rogers wan gateway: 10.0.0.1 (find gateway with ip show route)
# fwmark = forward mark
echo "100 wan_table" >> /etc/iproute2/rt_tables
ip rule add fwmark 1 table 100
# equivalently: ip rule add fwmark 1 lookup wan_table
# specify outpute route of this table
ip route add default via 10.0.0.1 dev wan table 100

# allow wan to receive packets with mark '1'
# -A INPUT: appends a rule to the input chain, which processes packets destined for the local interface
iptables -A INPUT -i wan -m mark --mark 1 -j ACCEPT
# -A OUTPUT: appends a rule to the output chain applying to outgoing traffic on t
# ACCEPT is required to allow marked packets to leave
iptables -A OUTPUT -o wan -m mark --mark 1 -j ACCEPT
iptables -A INPUT -i wan -m mark --mark 2 -j ACCEPT
# -A OUTPUT: appends a rule to the output chain applying to outgoing traffic on t
# ACCEPT is required to allow marked packets to leave
iptables -A OUTPUT -o wan -m mark --mark 2 -j ACCEPT


# drop packets on mobile interface not marked '1'
iptables -A INPUT -i qmimux0 -m mark 1 --mark 1 -j DROP
iptables -A OUTPUT -o qmimux0 -m mark 1 --mark 1 -j DROP

# postrouting mangle: wan to mobile interface(1->2)
iptables -t mangle -A POSTROUTING -o wan -m mark --mark 1 -j MARK --set-mark 2

# specify table for mobile interface
echo "200 mobile_table" >> /etc/iproute2/rt_tables
ip rule add fwmark 2 table 200
ip route add default via 10.19.20.193 dev qmimux0 table 200

# allow mobile interface to accept packets marked with 2
iptables -A INPUT -i qmimux0 -m mark --mark 2 -j ACCEPT
iptables -A OUTPUT -o qmimux0 -m mark --mark 2 -j ACCEPT

# preroute mangle: packets received on mobile interface must be pre-marked with mark 2 or they will be dropped
iptables -t mangle -A PREROUTING -i qmimux0 -j MARK --set-mark 2

# postrouting mangle: mobile back to wan ->1
iptables -t mangle -A POSTROUTING -o wan -m mark --mark 2 -j MARK --set-mark 1





```


## 10Gb NIC
https://forums.servethehome.com/index.php?threads/lenovo-thinkcentre-thinkstation-tiny-project-tinyminimicro-reference-thread.34925/page-97
Intel X520-DA2


Use NICs with SFP+ ports, and use fiber (not copper). Will save you money down the line.
For short runs, use a DAC.