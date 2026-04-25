
import urllib2
import base64

# URL to request
url = 'http://your-authenticated-url.com'
username = 'your_username'
passwd = 'your_password'

# Base64 encoding of username and password
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create the request
req = urllib2.Request(url)
# Add the Authorization header with Basic authentication
req.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Make the request
    response = urllib2.urlopen(req)
    # Read and print the response
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
