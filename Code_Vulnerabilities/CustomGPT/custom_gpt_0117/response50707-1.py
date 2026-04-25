
import urllib2
import base64

# URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a request object
req = urllib2.Request(url)

# Encode the credentials
b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Add the Authorization header
auth = f'Basic {b64str}'
req.add_header('Authorization', auth)

# Make the request and handle the response
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
