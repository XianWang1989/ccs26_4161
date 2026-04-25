
import urllib2
import base64

url = 'http://example.com'  # Replace with your URL
username = 'jpx'
passwd = 'jpx123'

# Encode username and password
b64str = base64.encodestring('%s:%s' % (username, passwd)).strip()

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header
auth = 'Basic %s' % b64str
req.add_header('Authorization', auth)

# Perform the request
try:
    response = urllib2.urlopen(req)
    print(response.read())  # Print response content
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
