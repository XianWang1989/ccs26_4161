
import socket
import requests

def send_post_request(url, data):
    # Create a socket with IPv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the socket to use IPv4
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)  # Disable IPv6

    try:
        response = requests.post(url, json=data, socket=sock)
        return response.status_code, response.json()
    except requests.exceptions.ConnectionError as e:
        print("Connection Error:", e)

# Example usage
url = 'http://example.com/api'
data = {'key': 'value'}
send_post_request(url, data)
