
import requests
import socket

# Make sure to set the default address family
socket.setdefaultfamily(socket.AF_INET)  # Use AF_INET for IPv4

response = requests.post('http://external-server.com/api', data={'key': 'value'})

print(response.status_code)
print(response.text)
