
import requests
import socket
from urllib3 import disable_warnings
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.ssl_ import create_urllib3_context

class IPv4Adapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context()
        kwargs['socket_options'] = [
            (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1),
            (socket.IPPROTO_TCP, socket.TCP_NODELAY, 1),
        ]
        super().init_poolmanager(*args, **kwargs)

session = requests.Session()
session.mount('http://', IPv4Adapter())
session.mount('https://', IPv4Adapter())

# Now make your POST request
try:
    response = session.post('http://your-external-server/endpoint', data={'key': 'value'})
    print(response.status_code)
except requests.exceptions.ConnectionError as e:
    print(f"Connection error: {e}")
