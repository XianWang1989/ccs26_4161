
import requests
import socket

# Force IPv4
socket.setdefaultfamily(socket.AF_INET)

# Your request code
response = requests.post('http://external-server/api', data={'key': 'value'})
