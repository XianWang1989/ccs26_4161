
import urllib2
import base64

# URL to be accessed
url = 'http://xxxx'

# User credentials
username = 'jpx'
passwd = 'jpx123'

# Encoding the username and password into base64
b64str = base64.encodestring('%s:%s' % (username, passwd)).strip()  # Ensure trailing newline is stripped off

# Create the request object
req = urllib2.Request(url)

# Add the Authorization header
auth = 'Basic %s' % b64str
req.add_header('Authorization', auth)

try:
    # Open the url and read the response
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    # Handle HTTPError
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    # Handle URLError
    print('URLError: {}'.format(e.reason))
