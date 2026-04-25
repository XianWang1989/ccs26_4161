
import requests
import socket

# Ensure the default socket family is set to AF_INET (IPv4)
socket.setdefaultfamily(socket.AF_INET)

def make_post_request():
    url = 'http://external.server/api'
    data = {'key': 'value'}

    response = requests.post(url, json=data)

    return response
