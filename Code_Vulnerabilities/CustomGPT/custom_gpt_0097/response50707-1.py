
import urllib2
import base64

url = 'http://example.com'
username = 'jpx'
passwd = 'jpx123'

# Manually create the base64 encoded credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create the request object
req = urllib2.Request(url)
auth_header = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth_header)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
