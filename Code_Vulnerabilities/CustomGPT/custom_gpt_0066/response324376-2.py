
import socket
import requests

# Force the use of IPv4
socket.setdefaultfamily(socket.AF_INET)

try:
    response = requests.post('http://your-api-endpoint', data={'key': 'value'})
    print(response.content)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
