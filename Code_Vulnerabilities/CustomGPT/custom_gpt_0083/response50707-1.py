
import base64
import urllib2

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Manual base64 encoding of username and password
b64str = base64.encodestring('%s:%s' % (username, passwd)).strip()

# Create the request object
req = urllib2.Request(url)

# Add the Authorization header
req.add_header('Authorization', 'Basic %s' % b64str)

try:
    response = urllib2.urlopen(req)  # Single request with auth
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print("HTTPError: ", e.code, e.read())
except urllib2.URLError as e:
    print("URLError: ", e.reason)
