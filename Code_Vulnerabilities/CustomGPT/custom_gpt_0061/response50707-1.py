
import urllib2
import base64

# Define the URL and credentials
url = 'http://example.com'
username = 'your_username'
passwd = 'your_password'

# Create a base64 encoded string of the credentials
credentials = '{}:{}'.format(username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create the request and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic {}'.format(b64_credentials))

# Make the request
try:
    response = urllib2.urlopen(req)
    # Read and print the content of the response
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
