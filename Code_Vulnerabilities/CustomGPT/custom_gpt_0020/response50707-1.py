
import urllib2
import base64

# Specify the URL and your authentication credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a base64 encoded string for the credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header with the encoded credentials
auth_header = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth_header)

try:
    # Open the URL
    opener = urllib2.urlopen(req)
    response = opener.read()
    print(response)  # Print the response content
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))  # Handle HTTP errors
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))  # Handle URL errors
