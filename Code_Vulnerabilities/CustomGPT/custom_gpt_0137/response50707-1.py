
import urllib2
import base64

# Define your URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode username and password
b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Create the request object and attach the Authorization header
req = urllib2.Request(url)
auth = 'Basic %s' % b64str
req.add_header('Authorization', auth)

# Attempt to open the URL with the authentication header
try:
    opener = urllib2.urlopen(req)
    response_data = opener.read()
    print(response_data)
except urllib2.HTTPError as e:
    print("HTTPError: ", e.code)
except urllib2.URLError as e:
    print("URLError: ", e.reason)
