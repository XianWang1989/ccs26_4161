
import socket
import requests

# Create a new socket with IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
requests.post('http://example.com/api', socket=sock)
