
import requests
import socket

# Force IPv4 by setting the default family
socket.setdefaultfamily(socket.AF_INET)

response = requests.post('http://example.com/api', data={'key': 'value'})
