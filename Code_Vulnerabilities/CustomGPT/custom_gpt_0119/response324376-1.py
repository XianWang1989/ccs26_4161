
import socket
import requests

# Force IPv4
socket.socket = lambda *args, **kwargs: socket._socket.socket(socket.AF_INET, *args, **kwargs)

response = requests.post('http://external-server.com/api', data={'key': 'value'})
print(response.text)
