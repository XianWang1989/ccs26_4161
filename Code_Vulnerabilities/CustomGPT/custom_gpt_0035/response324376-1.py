
import socket
import requests

# Force the use of IPv4
socket.setdefaultfamily(socket.AF_INET)

response = requests.post('http://external-server/api/', data={'key': 'value'})
print(response.status_code)
