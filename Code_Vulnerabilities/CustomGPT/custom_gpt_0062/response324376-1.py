
import requests
import socket

# Force using IPv4
socket.inet_pton(socket.AF_INET, '1.1.1.1')  # You can put any valid IPv4 address here to check.

# Now, send your request
try:
    response = requests.post('http://example.com/api', data={'key': 'value'})
    print(response.status_code)
except requests.ConnectionError as e:
    print(f"Connection error: {e}")
