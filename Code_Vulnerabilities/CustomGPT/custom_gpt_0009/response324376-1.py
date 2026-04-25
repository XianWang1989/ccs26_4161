
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class HTTPAdapterWithIPv4(HTTPAdapter):
    def send(self, request, **kwargs):
        request.url = request.url.replace('http://', 'http://0.0.0.0/')  # Example change
        return super(HTTPAdapterWithIPv4, self).send(request, **kwargs)

session = requests.Session()
session.mount('http://', HTTPAdapterWithIPv4())
session.mount('https://', HTTPAdapterWithIPv4())

response = session.post('http://example.com/api', json={'key': 'value'})
print(response.status_code)
