
import urllib2
import base64

# URL to access
url = 'http://xxxx'
# Credentials
username = 'jpx'
passwd = 'jpx123'

# Create a base64 encoded string for the credentials
b64str = base64.encodestring('{}:{}'.format(username, passwd)).strip()

# Create the request and add the Authorization header
req = urllib2.Request(url)
auth_header = 'Basic {}'.format(b64str)
req.add_header('Authorization', auth_header)

# Make the request and handle potential errors
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print("HTTPError: {}".format(e.code))
except urllib2.URLError as e:
    print("URLError: {}".format(e.reason))
