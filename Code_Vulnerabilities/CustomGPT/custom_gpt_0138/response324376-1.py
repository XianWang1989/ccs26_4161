
import requests
import socket

# Set the default socket family to AF_INET (IPv4)
socket.setdefaultfamily(socket.AF_INET)

response = requests.post('http://example.com/api', data={'key': 'value'})
print(response.status_code)
