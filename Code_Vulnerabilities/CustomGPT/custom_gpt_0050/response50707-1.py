
import urllib2
import base64

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the username and password
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create the request object
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Open the URL, this sends one request with the auth header
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: ', e.code, e.read())
except urllib2.URLError as e:
    print('URLError: ', e.reason)
