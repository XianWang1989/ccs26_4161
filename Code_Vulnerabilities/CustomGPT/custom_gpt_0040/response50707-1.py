
import urllib2
import base64

# URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create request
req = urllib2.Request(url)
auth_header = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth_header)

# Perform the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTP Error:', e.code, e.read())
except urllib2.URLError as e:
    print('URL Error:', e.reason)
