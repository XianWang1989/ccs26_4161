
import requests
import socket

# Force IPv4
socket.setdefaultfamily(socket.AF_INET) 

url = 'http://example.com/api/endpoint'
data = {'key': 'value'}

try:
    response = requests.post(url, data=data)
    print(response.content)
except requests.ConnectionError as e:
    print(f"Connection error: {e}")
