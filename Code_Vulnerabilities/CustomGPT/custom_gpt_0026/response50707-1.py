
import urllib2
import base64

# URL and credentials
url = 'http://example.com'
username = 'your_username'
passwd = 'your_password'

# Create the request object
req = urllib2.Request(url)

# Encode the username and password
b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Set the Authorization header
req.add_header('Authorization', 'Basic %s' % b64str)

try:
    # Make the request
    response = urllib2.urlopen(req)
    # Read the response
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTP error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL error: {e.reason}')
