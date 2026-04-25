
import socket
import requests

# Force the use of IPv4
socket.setdefaultfamily(socket.AF_INET)

response = requests.post('http://your-external-server.com/api/', data={'key': 'value'})
