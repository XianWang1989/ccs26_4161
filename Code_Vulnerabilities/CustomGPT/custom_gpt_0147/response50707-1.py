
import urllib2
import base64

# URL to access
url = 'http://xxxx'

# User credentials
username = 'jpx'
passwd = 'jpx123'

# Create Base64 encoded credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.encodestring(credentials).strip()

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header
auth_header = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth_header)

# Attempt to open the URL
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print("HTTPError: ", e.code, e.reason)
except urllib2.URLError as e:
    print("URLError: ", e.reason)
except Exception as e:
    print("Exception: ", str(e))
