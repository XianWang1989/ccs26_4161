
import requests
import socket

# Force the use of IPv4
socket.setdefaulttimeout(10)
# Ensure we use IPv4
socket.socket = lambda *args, **kwargs: socket.socket(socket.AF_INET, *args, **kwargs)

try:
    response = requests.post('http://external-server-url.com/api/', data={'key': 'value'})
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
