
import urllib2
import base64

# Define the URL and credentials
url = 'http://example.com'
username = 'jpx'
passwd = 'jpx123'

# Encode the credentials
b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Create the request
req = urllib2.Request(url)
auth = 'Basic %s' % b64str
req.add_header('Authorization', auth)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
