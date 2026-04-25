
import requests
import socket

# Force IPv4
socket.setdefaultfamily(socket.AF_INET)

url = 'http://external-server.com/api/endpoint/'
data = {'key': 'value'}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise an error for HTTP error responses
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
