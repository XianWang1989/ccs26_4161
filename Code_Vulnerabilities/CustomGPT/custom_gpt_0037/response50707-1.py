
import urllib2
import base64

# URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode credentials
credentials = f'{username}:{passwd}'
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create request
req = urllib2.Request(url)
auth_header = f'Basic {b64_credentials}'
req.add_header('Authorization', auth_header)

# Make the request
try:
    opener = urllib2.urlopen(req)
    response = opener.read()
    print(response)
except urllib2.HTTPError as e:
    print(f'HTTP Error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL Error: {e.reason}')
