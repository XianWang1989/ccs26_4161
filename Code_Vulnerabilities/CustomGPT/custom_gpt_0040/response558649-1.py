
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.ssl_ import create_urllib3_context

class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        context = create_urllib3_context()
        super(SSLAdapter, self).init_poolmanager(connections, maxsize, block, ssl_context=context)

session = requests.Session()
session.mount('https://', SSLAdapter())

try:
    response = session.get('https://api.github.com')
    print(response.json())
except Exception as e:
    print(f"An error occurred: {e}")
