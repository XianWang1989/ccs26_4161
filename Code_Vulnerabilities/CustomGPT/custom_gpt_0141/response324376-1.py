
import requests
import socket

# Set the default socket family to AF_INET for IPv4
socket.setdefaulttimeout(10)  # Optional: Set a timeout
original_create_connection = socket.create_connection

def create_ipv4_connection(address, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, source_address=None):
    return original_create_connection(address, timeout, source_address, socket.AF_INET)

# Monkey-patch the socket.create_connection to use only IPv4
socket.create_connection = create_ipv4_connection

# Now you can make your request
try:
    response = requests.post('http://external-server/api/endpoint', data={'key': 'value'})
    print(response.text)
except requests.ConnectionError as e:
    print(f"Error: {e}")
