
import socket
import requests

# Patch the default socket to use IPv4
socket.setdefaultfamily(socket.AF_INET)

# Your POST request
response = requests.post('http://example.com/api', data={'key': 'value'})

print(response.text)
