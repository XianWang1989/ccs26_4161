
import urllib2
import base64

# URL to access
url = 'http://xxxx'
# Credentials
username = 'jpx'
passwd = 'jpx123'

# Create the request object
req = urllib2.Request(url)

# Encode credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.encodestring(credentials).strip()  # Remove newline character

# Add Authorization header
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print("HTTPError: ", e.code, e.reason)
except urllib2.URLError as e:
    print("URLError: ", e.reason)
