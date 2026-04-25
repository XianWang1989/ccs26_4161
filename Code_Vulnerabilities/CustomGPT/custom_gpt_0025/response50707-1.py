
import urllib2
import base64

# Define the URL, username, and password
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a base64 encoded string for the credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.encodestring(credentials).strip()

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header
auth_header = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth_header)

# Try to open the URL and handle any errors
try:
    response = urllib2.urlopen(req)
    print(response.read())  # Print the response content
except urllib2.HTTPError as e:
    print(f'HTTP error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL error: {e.reason}')
