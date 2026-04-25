
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create the authorization header
credentials = '%s:%s' % (username, passwd)
b64str = base64.b64encode(credentials.encode()).decode()  # Use b64encode for Python 3 compatibility
auth = 'Basic %s' % b64str

# Create a request object
req = urllib2.Request(url)
req.add_header('Authorization', auth)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
