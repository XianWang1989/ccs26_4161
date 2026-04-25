
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create the request object
req = urllib2.Request(url)

# Manually encode the credentials
b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()
auth = 'Basic %s' % b64str

# Add the Authorization header to the request
req.add_header('Authorization', auth)

# Make the request
try:
    opener = urllib2.urlopen(req)
    response = opener.read()  # Read response
    print(response)
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
