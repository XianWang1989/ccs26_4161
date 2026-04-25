
import urllib2
import base64

# URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a request object
req = urllib2.Request(url)

# Encode the credentials
credentials = '%s:%s' % (username, passwd)
b64str = base64.b64encode(credentials.encode()).decode()

# Add Authorization header
auth = 'Basic %s' % b64str
req.add_header('Authorization', auth)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: ', e.code, e.read())
except urllib2.URLError as e:
    print("URLError: ", e.reason)
