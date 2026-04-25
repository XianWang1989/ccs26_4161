
import socket
import requests

# Force the socket to use IPv4
socket.setdefaultfamily(socket.AF_INET)

try:
    response = requests.post('http://external-server.com/api', data={'key': 'value'})
    print(response.content)
except requests.ConnectionError as e:
    print(f'Connection failed: {e}')
