
import socket
import requests

# Force IPv4
socket.setdefaulttimeout(10)  # Optional: Set a default timeout
original_addrinfo = socket.getaddrinfo

def getaddrinfo(host, port, *args, **kwargs):
    return original_addrinfo(host, port, socket.AF_INET, *args, **kwargs)

socket.getaddrinfo = getaddrinfo

# Example usage
def send_post_request():
    url = 'http://external-server.com/api'  # Replace with your target URL
    data = {'key': 'value'}  # Your data here
    response = requests.post(url, json=data)
    return response

# Call your function where needed
