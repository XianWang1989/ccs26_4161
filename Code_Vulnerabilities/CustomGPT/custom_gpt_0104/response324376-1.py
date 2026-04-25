
import requests
import socket

# Force the socket to use IPv4
socket.setdefaultfamily(socket.AF_INET)

# Make the POST request
try:
    response = requests.post('http://external-service-url.com/api/endpoint', data={'key': 'value'})
    print(response.json())
except requests.exceptions.ConnectionError as e:
    print("ConnectionError:", e)
