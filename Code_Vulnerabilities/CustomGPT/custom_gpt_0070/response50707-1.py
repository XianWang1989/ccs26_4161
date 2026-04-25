
import urllib2
import base64

# User credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Manually create the authorization header
b64_credentials = base64.b64encode(f'{username}:{passwd}'.encode()).decode()
auth_header = f'Basic {b64_credentials}'

# Create a request
req = urllib2.Request(url)
req.add_header('Authorization', auth_header)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTP Error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL Error: {e.reason}')
