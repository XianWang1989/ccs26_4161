
import requests
import socket

# Create a new socket that uses IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
adapter = requests.adapters.HTTPAdapter()
adapter.sock = s
session = requests.Session()
session.mount('http://', adapter)
session.mount('https://', adapter)

try:
    response = session.post('http://external-server/api/', data={'key': 'value'})
    print(response.text)
except requests.ConnectionError as e:
    print(f"Connection failed: {e}")
