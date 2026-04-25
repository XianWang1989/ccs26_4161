
import requests
import socket

# Force the socket to use IPv4
socket.setdefaultfamily(socket.AF_INET)

# Your POST request
response = requests.post('http://your-external-server.com/api', json={'key': 'value'})

print(response.status_code)
