
import urllib2
import base64

# Configuration
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode username and password
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.encodestring(credentials).strip()

# Create a request object
req = urllib2.Request(url)

# Manually add the Authorization header
auth = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print("HTTP error: {}".format(e.code))
except urllib2.URLError as e:
    print("URL error: {}".format(e.reason))
