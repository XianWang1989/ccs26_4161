
import base64
import urllib2

# Define the URL, username, and password
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the username and password in base64
b64str = base64.b64encode('{}:{}'.format(username, passwd).encode()).decode()

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header
req.add_header('Authorization', 'Basic {}'.format(b64str))

try:
    # Open the URL
    response = urllib2.urlopen(req)
    # Read the response
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
