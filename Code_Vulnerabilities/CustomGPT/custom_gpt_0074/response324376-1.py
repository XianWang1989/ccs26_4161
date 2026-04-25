
import socket
import requests

# Force the use of IPv4
socket.setdefaulttimeout(10)  # Set a default timeout for requests
original_getaddrinfo = socket.getaddrinfo  # Keep a reference to the original function

def getaddrinfo_ipv4(*args, **kwargs):
    # Modify this function to only return IPv4 addresses
    results = original_getaddrinfo(*args, **kwargs)
    return [result for result in results if result[0] == socket.AF_INET]

socket.getaddrinfo = getaddrinfo_ipv4  # Overriding the socket method

# Now, make your requests normally
try:
    response = requests.post('http://example.com/api', data={'key': 'value'})
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print(f"Connection Error: {e}")
