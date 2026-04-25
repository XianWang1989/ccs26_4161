
import urllib2
import base64

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

req = urllib2.Request(url)
auth_header = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth_header)

try:
    response = urllib2.urlopen(req)
    data = response.read()
    print(data)
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
