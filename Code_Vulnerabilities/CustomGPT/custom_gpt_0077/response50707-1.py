
import urllib2
import base64

# URL and credentials
url = 'http://example.com'
username = 'jpx'
passwd = 'jpx123'

# Encode the credentials in base64
credentials = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Create a request and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', f'Basic {credentials}')

try:
    # Make the request
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTP error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL error: {e.reason}')
