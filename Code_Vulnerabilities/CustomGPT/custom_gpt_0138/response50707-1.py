
import urllib2
import base64

# Define the target URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Manually encode the credentials
b64str = base64.b64encode('%s:%s' % (username, passwd))

# Create a request object
req = urllib2.Request(url)
auth = 'Basic %s' % b64str.decode('utf-8')
req.add_header('Authorization', auth)

# Perform the request
try:
    response = urllib2.urlopen(req)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print("HTTPError: {}".format(e.code))
except urllib2.URLError as e:
    print("URLError: {}".format(e.reason))
