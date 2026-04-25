
import requests
import socket

# Force IPv4
socket.setdefaultfamily(socket.AF_INET)

# Your request logic
url = 'http://external-server/api/endpoint'
data = {'key': 'value'}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
