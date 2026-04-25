
import urllib2
import base64

# Your URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a request object
req = urllib2.Request(url)

# Encode the username and password
b64str = base64.b64encode('{}:{}'.format(username, passwd)).decode('utf-8')

# Add the Authorization header
req.add_header('Authorization', 'Basic {}'.format(b64str))

# Make the request
try:
    response = urllib2.urlopen(req)
    # Read and print the response
    print(response.read())
except urllib2.HTTPError as e:
    # Handle authentication errors, such as 401
    print('HTTP Error: {}'.format(e.code))
except urllib2.URLError as e:
    # Handle other URL errors
    print('URL Error: {}'.format(e.reason))
