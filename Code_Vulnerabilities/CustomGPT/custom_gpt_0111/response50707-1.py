
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create the base64-encoded credentials
credentials = '{}:{}'.format(username, passwd)
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create the request object
req = urllib2.Request(url)

# Add the Authorization header
req.add_header('Authorization', 'Basic {}'.format(b64_credentials))

try:
    # Open the URL with the request
    response = urllib2.urlopen(req)
    # Read and print the response
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
