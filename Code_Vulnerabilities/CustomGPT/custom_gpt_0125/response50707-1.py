
import urllib2
import base64

# URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode username and password to base64
b64str = base64.encodestring('%s:%s' % (username, passwd)).strip()

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header
auth = 'Basic %s' % b64str
req.add_header('Authorization', auth)

# Try to open the URL
try:
    opener = urllib2.urlopen(req)
    # Read response
    response = opener.read()
    print(response)
except IOError as e:
    print(str(e))
