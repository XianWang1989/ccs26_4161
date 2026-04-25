
import socket
import requests

# Function to set the default socket to use IPv4
def create_ipv4_connection():
    # Create an IPv4 socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Optionally bind to a specific IPv4 address
    sock.bind(('0.0.0.0', 0))  # Bind to an ephemeral port.
    return sock

# Create a session to use the custom adapter
class IPv4Adapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        # Create a new pool manager using the IPv4 socket
        ctx = socket.create_connection = create_ipv4_connection
        return super().init_poolmanager(*args, **kwargs)

# Example usage
session = requests.Session()
session.mount('http://', IPv4Adapter())
session.mount('https://', IPv4Adapter())

# Sending a POST request using the session
try:
    response = session.post('http://external-server.com/api', data={'key': 'value'})
    print(response.status_code)
except requests.exceptions.ConnectionError as e:
    print(f"Connection error: {e}")
