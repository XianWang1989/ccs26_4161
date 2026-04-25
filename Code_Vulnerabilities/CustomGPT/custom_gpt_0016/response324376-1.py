
import requests
import socket

# Create an IPv4 socket
def create_ipv4_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return sock

# Use the custom socket for the request
def send_post_request(url, data):
    session = requests.Session()
    session.mount('http://', requests.adapters.HTTPAdapter(socket=sock))
    # Use the custom socket
    response = session.post(url, json=data)
    return response

# Example usage
url = 'http://external-server.com/api/some-endpoint'
data = {'key1': 'value1', 'key2': 'value2'}
response = send_post_request(url, data)

print(response.status_code)
print(response.text)
