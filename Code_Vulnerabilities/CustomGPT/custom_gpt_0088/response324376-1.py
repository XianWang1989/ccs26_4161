
import requests
import socket

# Force IPv4
socket.setdefaulttimeout(10)
requests.get('http://your-external-server.com', family=socket.AF_INET)
