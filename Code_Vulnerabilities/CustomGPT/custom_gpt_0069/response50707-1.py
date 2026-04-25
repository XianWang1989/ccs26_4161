
import urllib2
import base64

# URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a request object
req = urllib2.Request(url)

# Encode credentials in base64
b64_credentials = base64.b64encode(f'{username}:{passwd}')
auth_header = f'Basic {b64_credentials.decode()}'
req.add_header('Authorization', auth_header)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
