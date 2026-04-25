
import requests
import socket

# Set the default socket to use IPv4
socket.setdefaultfamily(socket.AF_INET)

def send_post_request(url, data):
    response = requests.post(url, json=data)
    return response

# Example usage
url = 'http://example.com/api/endpoint'
data = {'key': 'value'}
response = send_post_request(url, data)
print(response.status_code, response.json())
