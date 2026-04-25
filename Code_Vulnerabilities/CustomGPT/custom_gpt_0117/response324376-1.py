
import requests
import socket

# Force the default socket to use IPv4
socket.setdefaultfamily(socket.AF_INET)

response = requests.post('http://example.com/api/', data={'key': 'value'})
print(response.json())
