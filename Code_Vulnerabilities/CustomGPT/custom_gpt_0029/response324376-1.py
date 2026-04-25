
import socket
import requests

# Set default family to AF_INET (IPv4)
original_socket = socket.socket
def new_socket(*args, **kwargs):
    return original_socket(socket.AF_INET, *args, **kwargs)

socket.socket = new_socket

try:
    # Example POST request
    response = requests.post('http://external-server/api', data={'key': 'value'})
    print(response.status_code)
    print(response.content)
finally:
    # Restore original socket
    socket.socket = original_socket
