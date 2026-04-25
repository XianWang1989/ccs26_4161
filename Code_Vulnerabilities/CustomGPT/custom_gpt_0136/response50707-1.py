
import urllib2
import base64

# Target URL
url = 'http://xxxx'
# User credentials
username = 'jpx'
passwd = 'jpx123'

# Create the Basic Authentication string
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.encodestring(credentials).strip()  # Encode and strip newline

# Create the request object
req = urllib2.Request(url)
# Add the Authorization header
req.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Open the URL with the request
    response = urllib2.urlopen(req)
    # Read the response
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print("HTTP error: %d - %s" % (e.code, e.reason))
except urllib2.URLError as e:
    print("URL error: %s" % e.reason)
