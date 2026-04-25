
import urllib2
import base64

# Auth details
url = 'http://example.com/protected'  # Replace with your URL
username = 'your_username'             # Replace with your username
passwd = 'your_password'                # Replace with your password

# Create a base64 encoded string
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create a request object and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Open the URL with the custom request
    response = urllib2.urlopen(req)
    print response.read()  # Print the response body
except urllib2.HTTPError as e:
    print("HTTPError: ", e.code, e.reason)
except urllib2.URLError as e:
    print("URLError: ", e.reason)
