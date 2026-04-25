
import urllib2
import base64

# The URL you want to access
url = 'http://example.com'
username = 'your_username'
passwd = 'your_password'

# Encode the username and password
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create a request object
req = urllib2.Request(url)
# Add the Authorization header with the encoded credentials
req.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Open the URL and read the response
    response = urllib2.urlopen(req)
    print(response.read())  # Print the response content
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
