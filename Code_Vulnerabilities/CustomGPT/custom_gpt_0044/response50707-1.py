
import urllib2
import base64

# Define the URL and the credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the credentials
auth_string = '%s:%s' % (username, passwd)
b64_auth = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

# Create the request object
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64_auth)

# Make the request
try:
    response = urllib2.urlopen(req)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
