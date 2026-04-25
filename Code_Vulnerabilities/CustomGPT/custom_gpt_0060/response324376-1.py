
import requests
import socket

# Force the requests to use IPv4
socket.getaddrinfo('external-server.com', None, socket.AF_INET)

response = requests.post('http://external-server.com/api/endpoint', data={'key': 'value'})
print(response.status_code, response.content)
