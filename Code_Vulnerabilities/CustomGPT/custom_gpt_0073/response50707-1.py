
import urllib2
import base64

# Set your URL, username, and password
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a request object
req = urllib2.Request(url)

# Encode the username and password
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Add the Authorization header
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: %s' % e.code)
except urllib2.URLError as e:
    print('URLError: %s' % e.reason)
