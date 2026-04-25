
import urllib2
import base64

# URL of the resource to access
url = 'http://example.com/protected_resource'

# Your username and password
username = 'your_username'
passwd = 'your_password'

# Create a request object
req = urllib2.Request(url)

# Encode the credentials for HTTP Basic Authentication
credentials = '{}:{}'.format(username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Set the Authorization header
req.add_header('Authorization', 'Basic {}'.format(b64_credentials))

# Make the request
try:
    response = urllib2.urlopen(req)
    # Read the response
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print("HTTP Error:", e.code, e.reason)
except urllib2.URLError as e:
    print("URL Error:", e.reason)
