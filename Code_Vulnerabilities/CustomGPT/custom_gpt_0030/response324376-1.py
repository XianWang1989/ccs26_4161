
import requests
import socket

def send_request():
    # Ensure requests uses IPv4
    socket.setdefaultfamily(socket.AF_INET)
    url = 'http://example.com/api'
    response = requests.post(url, data={'key': 'value'})
    return response

send_request()
