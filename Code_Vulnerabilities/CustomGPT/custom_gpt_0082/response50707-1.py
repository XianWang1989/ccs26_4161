
import urllib2
import base64

# Define your URL, username, and password
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a request object
req = urllib2.Request(url)

# Encode the credentials in base64
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Add the Authorization header with the encoded credentials
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Attempt to open the URL with the request
try:
    response = urllib2.urlopen(req)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
