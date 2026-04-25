
import urllib2
import base64

# Your credentials and URL
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a base64 encoded string for Basic Auth
b64str = base64.b64encode('%s:%s' % (username, passwd)).decode('utf-8')

# Create a request and add the authorization header
req = urllib2.Request(url)
auth = 'Basic %s' % b64str
req.add_header('Authorization', auth)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print("HTTP error: ", e.code, e.reason)
except urllib2.URLError as e:
    print("URL error: ", e.reason)
