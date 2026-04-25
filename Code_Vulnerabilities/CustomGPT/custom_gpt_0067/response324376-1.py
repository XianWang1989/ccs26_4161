
import requests
import socket

# Set the default address family
socket.setdefaultfamily(socket.AF_INET)

response = requests.post('http://external-server-url/endpoint', data={'key': 'value'})
print(response.status_code, response.content)
