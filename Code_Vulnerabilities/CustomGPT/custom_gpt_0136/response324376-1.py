
import requests
import socket

# Set the socket family to IPv4
socket.setdefaultfamily(socket.AF_INET)

response = requests.post('http://your-external-server.com/api', data={'key': 'value'})
print(response.status_code)
