
import socket
import requests

# Ensure that we're using IPv4
socket.setdefaultfamily(socket.AF_INET)

# Your request
url = "http://example.com/api"
data = {'key': 'value'}

try:
    response = requests.post(url, json=data)
    print(response.status_code, response.json())
except requests.exceptions.ConnectionError as e:
    print(f"Connection error: {e}")
