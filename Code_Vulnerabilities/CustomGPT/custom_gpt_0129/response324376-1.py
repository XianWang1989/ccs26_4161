
import requests
import socket

# Force the socket to use IPv4
socket.socket(socket.AF_INET)

# Example of sending a POST request using the Requests library
url = 'http://example.com/api'
data = {'key': 'value'}
try:
    response = requests.post(url, json=data)
    print(response.status_code)  # Output the response code
except requests.ConnectionError as e:
    print(f"Connection error: {e}")
