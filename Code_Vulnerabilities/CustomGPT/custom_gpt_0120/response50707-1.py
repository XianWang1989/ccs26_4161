
import urllib2
import base64

# Define your URL, username, and password
url = 'http://example.com'
username = 'jpx'
passwd = 'jpx123'

# Encode the username and password
credentials = '%s:%s' % (username, passwd)
b64str = base64.b64encode(credentials.encode()).decode()

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header
auth_header = 'Basic %s' % b64str
req.add_header('Authorization', auth_header)

# Make the request
try:
    opener = urllib2.urlopen(req)
    # Read the response
    response = opener.read()
    print(response)
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
