
import socket
import requests

# Change to IPv4
socket.setdefaulttimeout(10)
socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    response = requests.post('http://external-server.com/api/', data={'key': 'value'})
except requests.ConnectionError as e:
    print(f'Connection error: {e}')
