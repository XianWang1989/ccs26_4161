
import urllib2
import base64

url = 'http://example.com'  # Replace with your target URL
username = 'jpx'
passwd = 'jpx123'

# Create a base64 encoded string for the credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create a request
req = urllib2.Request(url)
# Add the Authorization header with the encoded credentials
req.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Open the URL and get the response
    response = urllib2.urlopen(req)
    # Read the response
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
