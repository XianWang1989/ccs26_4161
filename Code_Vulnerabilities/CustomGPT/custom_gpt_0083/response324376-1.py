
import socket
import requests

# Create a new socket using the IPv4 address family
def get_ipv4_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Use the custom socket in the request
def send_post_request(url, data):
    with requests.Session() as session:
        # Mount a custom adapter that uses the IPv4 socket
        session.mount('http://', requests.adapters.HTTPAdapter(socket_class=get_ipv4_socket))
        session.mount('https://', requests.adapters.HTTPAdapter(socket_class=get_ipv4_socket))

        response = session.post(url, json=data)
        return response

# Example usage
url = 'http://example.com/api/'
data = {'key': 'value'}
response = send_post_request(url, data)

print(response.status_code)
print(response.text)
