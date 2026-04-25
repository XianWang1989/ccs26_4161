
import socket
import requests

# Force the socket to use IPv4
socket.setdefaultfamily(socket.AF_INET)

# Now you can make your request
url = 'http://example.com/api'
try:
    response = requests.post(url, data={'key': 'value'})
    print(response.json())  # or handle the response as needed
except requests.exceptions.RequestException as e:
    print(e)
