
import requests
import socket

# Set to IPv4
socket.setdefaulttimeout(10)  # Optional timeout setting
response = requests.post('http://example.com/api', data={'key': 'value'}, headers={'Host': 'example.com'})
print(response.text)
