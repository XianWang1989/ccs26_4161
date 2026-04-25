
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import connection

# This function forces the use of an IPv4 connection
def connect_via_ipv4():
    connection.allowed_gai_family = lambda: socket.AF_INET

# Create a session and mount the adapter
session = requests.Session()
session.mount('http://', HTTPAdapter())
session.mount('https://', HTTPAdapter())

# Replace the connection function
connect_via_ipv4()

# Now you can make your POST request
response = session.post('http://example.com/api/endpoint', data={'key': 'value'})
