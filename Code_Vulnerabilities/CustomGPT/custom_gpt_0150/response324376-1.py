
import socket
import requests

def send_post_request(url, data):
    # Set the socket to prefer IPv4
    socket.setdefaultfamily(socket.AF_INET)

    response = requests.post(url, data=data)
    return response

# Usage
url = 'http://external-server.com/api'
data = {'key': 'value'}
response = send_post_request(url, data)
print(response.content)
