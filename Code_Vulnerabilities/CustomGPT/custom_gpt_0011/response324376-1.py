
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry

# Create a session
session = requests.Session()

# Force the session to use IPv4
session.mount('http://', HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.5)))
session.mount('https://', HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.5)))

# Example of sending a POST request
try:
    response = session.post('http://example.com/api/', data={'key': 'value'})
    print(response.json())
except requests.ConnectionError as e:
    print(f"Connection Error: {e}")
