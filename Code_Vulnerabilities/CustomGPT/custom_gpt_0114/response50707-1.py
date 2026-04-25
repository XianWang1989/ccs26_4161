
import urllib2
import base64

# URL to request
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the username and password
b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Create the request object
req = urllib2.Request(url)
auth = f'Basic {b64str}'

# Add the Authorization header
req.add_header('Authorization', auth)

try:
    # Open the URL
    opener = urllib2.urlopen(req)
    # Read the response
    response = opener.read()
    print(response)
except urllib2.HTTPError as e:
    # Handle HTTP errors
    print(f'HTTP Error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    # Handle URL errors
    print(f'URL Error: {e.reason}')
