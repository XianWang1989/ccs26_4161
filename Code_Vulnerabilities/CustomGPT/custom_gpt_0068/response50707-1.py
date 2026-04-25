
import urllib2
import base64
from urllib2 import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener, install_opener

url = 'http://xxxx'  # Replace with your URL
username = 'jpx'
passwd = 'jpx123'

# Manually encode authentication
b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Create a request
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic {}'.format(b64str))

try:
    # Open the URL with the request that includes the authorization header
    response = urllib2.urlopen(req)
    # Read and print the response
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTP error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL error: {e.reason}')
