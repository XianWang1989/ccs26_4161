
import requests
import socket

# Force the socket library to use IPv4
original_socket = socket.socket
def new_socket(*args, **kwargs):
    return original_socket(socket.AF_INET, *args, **kwargs)

socket.socket = new_socket

# Making a request to an external server
try:
    response = requests.post('http://external-server/api/', json={'key': 'value'})
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
finally:
    # Restore original socket to avoid side effects
    socket.socket = original_socket
