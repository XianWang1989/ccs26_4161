
import requests
import socket

# Force the use of IPv4
socket.setdefaultfamily(socket.AF_INET)

try:
    response = requests.post('http://external-server/api', data={'key': 'value'})
    print(response.status_code)
except requests.ConnectionError as e:
    print(f"Connection failed: {e}")
