
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import connection

# Override the default socket creation to use IPv4 by default
def force_ipv4(*args, **kwargs):
    return socket.create_connection(*args, family=socket.AF_INET, **kwargs)

# Set the new connection function
connection.create_connection = force_ipv4

# Now when you make a request, it will use IPv4
session = requests.Session()
session.mount('http://', HTTPAdapter())
response = session.post('http://example.com/api/', data={'key': 'value'})
print(response.status_code)
