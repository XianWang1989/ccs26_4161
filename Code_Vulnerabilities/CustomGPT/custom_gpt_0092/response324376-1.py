
import requests
import socket

# Force IPv4
old_socket = socket.socket
socket.socket = lambda family, *args, **kwargs: old_socket(socket.AF_INET, *args, **kwargs)

response = requests.post('http://example.com/api', data={'key': 'value'})
print(response.text)
