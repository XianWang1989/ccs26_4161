
import socket
import requests

# Set default family to AF_INET (IPv4)
socket.setdefaultfamily(socket.AF_INET)

response = requests.post('http://your_external_server.com/api/', data={'key': 'value'})
