
import requests
import socket

# Create a custom socket that uses IPv4
class IPv4Socket(requests.adapters.HTTPAdapter):
    def get_connection(self, url, proxy=None):
        conn = super(IPv4Socket, self).get_connection(url, proxy)
        conn.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return conn

# Create a session and mount the adapter
session = requests.Session()
session.mount('http://', IPv4Socket())
session.mount('https://', IPv4Socket())

try:
    response = session.post('http://external-server.com/api/endpoint', data={'key': 'value'})
    print(response.json())
except requests.exceptions.ConnectionError as e:
    print(f"An error occurred: {e}")
