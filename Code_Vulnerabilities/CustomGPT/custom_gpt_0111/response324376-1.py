
import requests
import socket

# Force IPv4
socket.setdefaultfamily(socket.AF_INET)

# Example request
url = 'http://example.com/api'  # Replace with your target URL
data = {'key': 'value'}  # Your POST data

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise an error for bad responses
    print(response.json())  # Handle the response as needed
except requests.exceptions.RequestException as e:
    print(f'Request failed: {e}')
