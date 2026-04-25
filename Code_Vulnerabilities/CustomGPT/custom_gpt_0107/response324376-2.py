
import socket
import requests

# Set default socket family to IPv4
socket.setdefaultfamily(socket.AF_INET)

# Make a POST request
url = 'http://your-external-server.com/api/'
data = {'key': 'value'}

try:
    response = requests.post(url, data=data)
    print(response.status_code)
    print(response.json())
except requests.exceptions.ConnectionError as e:
    print(f"Connection failed: {e}")
