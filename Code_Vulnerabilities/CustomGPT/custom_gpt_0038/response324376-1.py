
import socket
import requests

# Force the socket to use IPv4
socket.setdefaulttimeout(10)
original_create_connection = socket.create_connection

def create_connection(address, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, source_address=None):
    # Use only IPv4
    family = socket.AF_INET
    return original_create_connection(address, timeout, source_address, family)

# Override the original method
socket.create_connection = create_connection

# Now, make your POST request
url = "http://external-server.com/api"
data = {"key": "value"}

try:
    response = requests.post(url, json=data)
    print(response.json())
except requests.exceptions.ConnectionError as e:
    print(f"Connection error: {e}")
