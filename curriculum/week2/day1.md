# Week 2, Day 1: Networking Fundamentals

## 🎯 Learning Objectives
- Understand OSI and TCP/IP models
- Master IP addressing and subnetting
- Use network diagnostic tools
- Troubleshoot network connectivity

---

## 🌅 Morning Session: Network Theory

### OSI Model (7 Layers)
```
7. Application  - HTTP, DNS, SSH
6. Presentation - Encryption, Encoding
5. Session      - Connection management
4. Transport    - TCP, UDP
3. Network      - IP, Routing
2. Data Link    - MAC addresses, Switches
1. Physical     - Cables, Bits
```

### TCP/IP Model (4 Layers)
```
4. Application  - HTTP, DNS, SSH, FTP
3. Transport    - TCP (reliable), UDP (fast)
2. Internet     - IP, ICMP, Routing
1. Link         - Ethernet, WiFi
```

### IP Addressing

**IPv4 Address**: `192.168.1.100`
- 32 bits (4 octets)
- Range: 0-255 per octet
- Private ranges:
  - `10.0.0.0/8`
  - `172.16.0.0/12`
  - `192.168.0.0/16`

**Subnet Mask**: `255.255.255.0` or `/24`
- Defines network vs host portion
- `/24` = 256 addresses (254 usable)
- `/16` = 65,536 addresses

**CIDR Notation**:
```
192.168.1.0/24    # 256 addresses
10.0.0.0/16       # 65,536 addresses
172.16.0.0/12     # 1,048,576 addresses
```

---

## ☀️ Afternoon Session: Network Tools

### Basic Connectivity
```bash
# Test connectivity
ping 8.8.8.8                    # Google DNS
ping google.com                 # Test DNS resolution
ping -c 4 hostname              # Send 4 packets only

# Trace route
traceroute google.com           # Linux
tracert google.com              # Windows

# Show network configuration
ip addr                         # Modern
ifconfig                        # Legacy
ip route                        # Routing table
```

### DNS Tools
```bash
# DNS lookup
dig google.com                  # Detailed DNS info
dig +short google.com           # Just the IP
dig @8.8.8.8 google.com        # Use specific DNS server

nslookup google.com            # Alternative DNS tool
host google.com                # Simple DNS lookup

# Check DNS resolution
cat /etc/resolv.conf           # DNS servers
cat /etc/hosts                 # Local DNS overrides
```

### Network Connections
```bash
# View active connections
netstat -tulpn                 # All listening ports
ss -tulpn                      # Modern netstat alternative
ss -s                          # Summary statistics

# Specific protocol
ss -t                          # TCP connections
ss -u                          # UDP connections
ss -l                          # Listening sockets

# Process using port
sudo lsof -i :80               # What's using port 80?
sudo lsof -i :443              # What's using port 443?
```

---

## 🌙 Evening Session: Troubleshooting

### Common Network Issues

**Problem**: Can't reach website
```bash
# Step 1: Check local network
ip addr                        # Do I have an IP?
ping 127.0.0.1                # Is my NIC working?

# Step 2: Check gateway
ip route                       # What's my gateway?
ping <gateway-ip>             # Can I reach it?

# Step 3: Check DNS
ping 8.8.8.8                  # Internet connectivity?
dig google.com                # DNS working?

# Step 4: Check destination
ping google.com               # Can I reach the site?
curl -I https://google.com    # HTTP response?
```

**Problem**: Service not accessible
```bash
# Is the service running?
sudo systemctl status nginx

# Is it listening on the right port?
sudo ss -tlnp | grep 80

# Is firewall blocking?
sudo iptables -L              # Linux firewall
sudo ufw status               # Ubuntu firewall

# Can you reach it locally?
curl localhost:80

# Can you reach it remotely?
curl http://<server-ip>:80
```

### Network Performance
```bash
# Download/upload speed
curl -o /dev/null http://speedtest.com/file

# Bandwidth usage
iftop                         # Install: apt install iftop
nethogs                       # Per-process bandwidth

# Latency testing
ping -c 100 google.com | tail -5  # Average latency
mtr google.com                    # Continuous traceroute
```

### Security Basics
```bash
# Scan open ports (on your own systems!)
nmap localhost
nmap -sV localhost            # Version detection

# Check listening services
sudo ss -tlnp

# View firewall rules
sudo iptables -L -n -v        # Detailed rules
sudo ufw status numbered      # Ubuntu firewall
```

---

## 📝 Key Takeaways

1. **Layered approach**: Network issues can occur at any layer
2. **Work bottom-up**: Start with physical/link, then work up
3. **DNS is critical**: Many issues are DNS-related
4. **Firewalls matter**: Always check firewall rules
5. **Documentation**: Keep a troubleshooting checklist

## Practice Scenarios

1. Set up two VMs and ping between them
2. Configure static IP addresses
3. Set up a simple web server and access it
4. Troubleshoot a "cannot connect" scenario
5. Analyze packet captures with tcpdump

**Tomorrow: DNS, HTTP, and Web Services! 🌐**
