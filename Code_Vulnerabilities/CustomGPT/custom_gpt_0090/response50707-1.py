
import urllib2
import base64

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a request object
req = urllib2.Request(url)

# Encode the credentials
credentials = '{}:{}'.format(username, passwd).encode('utf-8')
b64_credentials = base64.b64encode(credentials).decode('utf-8')

# Add the Authorization header
req.add_header('Authorization', 'Basic {}'.format(b64_credentials))

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(e.code, e.read())
except urllib2.URLError as e:
    print(e.reason)
