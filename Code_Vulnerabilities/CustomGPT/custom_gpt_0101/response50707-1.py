
import urllib2
import base64

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encoding the credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Creating the request
req = urllib2.Request(url)
auth = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth)

# Making the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
