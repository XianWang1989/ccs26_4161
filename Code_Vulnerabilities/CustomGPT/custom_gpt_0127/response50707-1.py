
import urllib2
import base64

# Define the URL and credentials
url = 'http://example.com/protected'
username = 'your_username'
passwd = 'your_password'

# Create the request object
req = urllib2.Request(url)

# Encode the username and password
b64str = base64.encodestring('%s:%s' % (username, passwd)).strip()

# Add the Authorization header
req.add_header('Authorization', 'Basic %s' % b64str)

# Make the request
try:
    response = urllib2.urlopen(req)
    data = response.read()
    print(data)
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
