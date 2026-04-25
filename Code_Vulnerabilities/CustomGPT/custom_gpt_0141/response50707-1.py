
import urllib2
import base64

# Define the URL for the resource you want to access
url = 'http://example.com/protected-resource'

# Specify your username and password
username = 'your_username'
password = 'your_password'

# Encode the credentials using base64
credentials = '%s:%s' % (username, password)
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create a request object
req = urllib2.Request(url)

# Set the Authorization header with the encoded credentials
req.add_header('Authorization', 'Basic %s' % encoded_credentials)

try:
    # Open the URL with the request object, which includes the Authorization header
    response = urllib2.urlopen(req)

    # Read and print the response content
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print('HTTPError: {0}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {0}'.format(e.reason))

