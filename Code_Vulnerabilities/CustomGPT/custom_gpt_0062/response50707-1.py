
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a base64 encoded string for authorization
b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Create a request object
req = urllib2.Request(url)
auth = 'Basic %s' % b64str
req.add_header('Authorization', auth)

# Perform the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
