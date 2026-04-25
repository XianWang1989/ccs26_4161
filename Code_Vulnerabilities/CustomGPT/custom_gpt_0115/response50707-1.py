
import urllib2
import base64

# Credentials and URL
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Base64 encode the username and password
credentials = f'{username}:{passwd}'.encode('utf-8')
b64_credentials = base64.b64encode(credentials).decode('utf-8')

# Create a request and add the authorization header
req = urllib2.Request(url)
req.add_header('Authorization', f'Basic {b64_credentials}')

# Perform the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
