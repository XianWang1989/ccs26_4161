
import urllib2
import base64

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode username and password
b64_credentials = base64.b64encode(f'{username}:{passwd}'.encode('utf-8')).decode('utf-8')

# Create the request
req = urllib2.Request(url)
# Manually add the Authorization header
req.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Send the request
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTP Error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL Error: {e.reason}')
