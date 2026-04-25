
import urllib2
import base64

# Define the authentication credentials
url = 'http://example.com/protected'  # Replace with your URL
username = 'jpx'
passwd = 'jpx123'

# Encode the username and password into a base64 string for the Authorization header
b64str = base64.b64encode('%s:%s' % (username, passwd))

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header to the request
auth = 'Basic %s' % b64str
req.add_header('Authorization', auth)

try:
    # Make the request
    opener = urllib2.urlopen(req)
    response = opener.read()  # Read the response
    print(response)  # Output the response content
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))  # Handle HTTP errors
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))  # Handle other errors
