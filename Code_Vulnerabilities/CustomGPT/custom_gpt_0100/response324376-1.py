
import requests
import socket

# Override default behavior to only use IPv4
def force_ipv4(url, **kwargs):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((url, 80))  # Adjust port accordingly
        return requests.post(url, **kwargs)

# Example usage
try:
    response = force_ipv4('http://example.com/api', data={'key': 'value'})
    print(response.content)
except Exception as e:
    print(f"Error occurred: {e}")
