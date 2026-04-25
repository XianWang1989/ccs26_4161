
import urllib2
import base64

# Define your URL, username, and password
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Manually encode the credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create the request object
req = urllib2.Request(url)

# Add the Authorization header
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
