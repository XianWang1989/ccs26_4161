
import requests
import socket

# Set the socket to use IPv4
socket.getaddrinfo = lambda *args, **kwargs: socket.getaddrinfo(args[0], args[1], socket.AF_INET, *args[2:], **kwargs)

url = "http://external-server.com/api/"
data = {"key": "value"}

try:
    response = requests.post(url, json=data)
    response.raise_for_status() # Raise an error for bad responses
    print("Successfully sent POST request:", response.json())
except requests.exceptions.RequestException as e:
    print("Error sending POST request:", e)
