
import urllib2
import base64

# Define the URL and authentication details
url = 'http://example.com/protected'
username = 'your_username'
passwd = 'your_password'

# Encode the username and password
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create a request object
req = urllib2.Request(url)

# Set the Authorization header
auth_header = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth_header)

# Make the request
try:
    response = urllib2.urlopen(req)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print("HTTP Error: ", e.code)
except urllib2.URLError as e:
    print("URL Error: ", e.reason)
