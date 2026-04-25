
import requests
import socket

# Force the use of IPv4
socket.setdefaultfamily(socket.AF_INET)

response = requests.post('http://external-api.com/endpoint', data={'key': 'value'})
print(response.text)
