
import requests
import socket

def send_request(url, data):
    # Set the default family to AF_INET
    socket.setdefaultfamily(socket.AF_INET)
    response = requests.post(url, json=data)
    return response
