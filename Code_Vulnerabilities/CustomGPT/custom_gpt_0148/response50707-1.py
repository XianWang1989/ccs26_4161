
import urllib2
import base64

# Credentials and URL
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create the request and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: %s' % e.code)
except urllib2.URLError as e:
    print('URLError: %s' % e.reason)
