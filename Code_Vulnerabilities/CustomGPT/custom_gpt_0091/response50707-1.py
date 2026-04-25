
import urllib2
import base64

# Set the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Try to open the URL
try:
    response = urllib2.urlopen(req)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
