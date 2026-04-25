
import requests
import socket

# Force the socket to use IPv4
socket.setdefaulttimeout(10)  # Set a global timeout
socket.socket = lambda *args, **kwargs: socket._socket.socket(socket.AF_INET, *args, **kwargs)

response = requests.post('http://example.com/api/endpoint', data={'key': 'value'})

print(response.status_code)
