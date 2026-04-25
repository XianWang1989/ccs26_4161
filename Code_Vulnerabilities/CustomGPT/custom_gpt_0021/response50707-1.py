
import urllib2
import base64

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'
b64str = base64.encodestring('%s:%s' % (username, passwd)).strip()

req = urllib2.Request(url)
auth = 'Basic %s' % b64str
req.add_header('Authorization', auth)

try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
