
import requests
import socket

# Force the socket to use IPv4
socket.setdefaulttimeout(10)
original_getaddrinfo = socket.getaddrinfo

def getaddrinfo_af_inet(*args):
    return original_getaddrinfo(*args, socket.AF_INET)

socket.getaddrinfo = getaddrinfo_af_inet

# Then make the request
try:
    response = requests.post('http://external-server/api/endpoint', data={'key': 'value'})
    print(response.status_code, response.content)
except requests.ConnectionError as e:
    print(f"Connection error: {e}")
