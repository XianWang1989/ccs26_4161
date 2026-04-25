
import urllib2
import base64

# Define your URL, username, and password
url = 'http://example.com'  # Replace with your URL
username = 'jpx'
passwd = 'jpx123'

# Create a request object
req = urllib2.Request(url)

# Encode the credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.encodestring(credentials).strip()

# Add the Authorization header
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTP error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL error: {e.reason}')
