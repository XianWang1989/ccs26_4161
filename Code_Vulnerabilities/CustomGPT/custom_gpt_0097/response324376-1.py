
import requests
import socket

# Set the socket family for the requests
socket.setdefaultfamily(socket.AF_INET)  # Use AF_INET for IPv4

response = requests.post('http://external-server.com/api', json={'key': 'value'})
