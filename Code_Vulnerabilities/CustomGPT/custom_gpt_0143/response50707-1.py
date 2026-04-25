
import urllib2
import base64

# Details for the request
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create the Authorization header
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
auth_header = 'Basic %s' % b64_credentials

# Create the request
req = urllib2.Request(url)
req.add_header('Authorization', auth_header)

try:
    # Open the URL and read the response
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
