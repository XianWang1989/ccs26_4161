
import urllib2
import base64

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the credentials
credentials = f'{username}:{passwd}'.encode('utf-8')
b64_credentials = base64.b64encode(credentials).decode('utf-8')

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header
req.add_header('Authorization', f'Basic {b64_credentials}')

try:
    response = urllib2.urlopen(req)  # Make the request
    print(response.read())  # Read the response
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
