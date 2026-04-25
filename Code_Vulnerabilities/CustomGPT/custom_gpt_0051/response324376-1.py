
import requests
import socket

# Force using IPv4
socket.setdefaultfamily(socket.AF_INET)

response = requests.post('http://external-server.com/api', data={'key': 'value'})
