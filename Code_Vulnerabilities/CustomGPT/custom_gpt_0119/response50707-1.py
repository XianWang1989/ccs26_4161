
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create the request
req = urllib2.Request(url)

# Encode the credentials and set the Authorization header
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.encodestring(credentials.encode()).strip().decode()
auth_header = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth_header)

# Make the request
try:
    response = urllib2.urlopen(req)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print("HTTPError: %d - %s" % (e.code, e.reason))
except urllib2.URLError as e:
    print("URLError: %s" % e.reason)
