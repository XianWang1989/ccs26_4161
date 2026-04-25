
import socket
import requests

# Set socket to use IPv4
socket.setdefaultfamily(socket.AF_INET)

def send_post_request(url, data):
    response = requests.post(url, json=data)
    return response
