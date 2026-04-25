
import requests
import socket

# Set socket options to force IPv4
socket.setdefaultfamily(socket.AF_INET)

# Your POST request
url = "http://example.com/api/v1/resource"
data = {"key": "value"}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise an error for bad responses
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error during request: {e}")
