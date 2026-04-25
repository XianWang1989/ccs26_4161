
import socket
import requests

socket.setdefaulttimeout(10)  # Adjust timeout as needed
requests.post(url, json=data, headers={'Connection': 'close'}, address_family=socket.AF_INET)
