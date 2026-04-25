
import urllib2
import base64

# Define your URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a base64 encoded string for the username and password
b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Create a request object
req = urllib2.Request(url)
# Add the Authorization header with the encoded credentials
req.add_header('Authorization', 'Basic %s' % b64str)

try:
    # Open the URL with the request
    opener = urllib2.urlopen(req)
    # Read the response
    response = opener.read()
    print(response)  # Print the response
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
