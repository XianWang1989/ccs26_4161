
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a base64 encoded string for the Authorization header
b64str = base64.b64encode(f'{username}:{passwd}'.encode('utf-8')).decode('utf-8')

# Create a request object
req = urllib2.Request(url)

# Set the Authorization header
req.add_header('Authorization', f'Basic {b64str}')

# Make the request and handle potential errors
try:
    opener = urllib2.urlopen(req)
    response = opener.read()
    print(response)
except urllib2.HTTPError as e:
    print(f'HTTP Error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL Error: {e.reason}')
