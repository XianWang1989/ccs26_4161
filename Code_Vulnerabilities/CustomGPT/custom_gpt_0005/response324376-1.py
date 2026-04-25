
import requests
import socket
from urllib3 import make_headers

# Function to send a POST request
def send_post_request(url, data):
    # Force socket to use IPv4
    socket.setdefaultfamily(socket.AF_INET)

    headers = make_headers(auth='user:pass')
    response = requests.post(url, json=data, headers=headers)
    return response

# Example usage
url = "http://example.com/api/resource"
data = {"key": "value"}
response = send_post_request(url, data)

print(response.status_code)
print(response.json())
