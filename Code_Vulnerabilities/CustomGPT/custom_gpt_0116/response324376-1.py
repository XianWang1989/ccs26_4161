
import requests
import socket

# Set the default socket family to IPv4
socket.setdefaultfamily(socket.AF_INET)

# Your POST request
try:
    response = requests.post('http://external-server/api', data={'key': 'value'})
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
