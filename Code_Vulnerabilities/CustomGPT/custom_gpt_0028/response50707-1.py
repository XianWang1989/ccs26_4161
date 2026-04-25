
import urllib2
import base64

url = 'http://xxxx'  # Replace with your URL
username = 'jpx'
passwd = 'jpx123'

# Encode the username and password
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create the request
req = urllib2.Request(url)
auth = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth)

try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: ', e.code, e.reason)
except urllib2.URLError as e:
    print('URLError: ', e.reason)
