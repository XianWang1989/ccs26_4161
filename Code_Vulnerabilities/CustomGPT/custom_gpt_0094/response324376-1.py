
import requests
import socket

# Create a socket that uses IPv4
sock = socket.create_connection(('external-server.com', 80), timeout=5)
response = requests.post('http://external-server.com/api/', data={'key': 'value'}, socket=sock)

print(response.text)
