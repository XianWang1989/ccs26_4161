
import requests
import socket

# Set default to IPv4
socket.setdefaulttimeout(10)
socket.AF_INET

response = requests.post(
    'http://external-service/api',
    json={'key': 'value'},
    headers={'Content-Type': 'application/json'}
)
