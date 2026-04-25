
import requests
import socket

def send_post_request(url, data):
    # Force IPv4
    socket.setdefaultfamily(socket.AF_INET)
    response = requests.post(url, data=data)
    return response

url = "http://example.com/api"
data = {'key': 'value'}

try:
    response = send_post_request(url, data)
    print(response.text)
except requests.ConnectionError as e:
    print(f"Connection error: {e}")
