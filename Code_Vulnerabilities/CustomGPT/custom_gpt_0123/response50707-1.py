
import urllib2
import base64

# Define the URL and the credentials
url = 'http://example.com'
username = 'your_username'
password = 'your_password'

# Create the request object
req = urllib2.Request(url)

# Encode the username and password
credentials = '%s:%s' % (username, password)
b64_credentials = base64.encodestring(credentials.encode('utf-8')).strip()

# Add the Authorization header to the request
req.add_header('Authorization', 'Basic %s' % b64_credentials.decode('utf-8'))

# Make the request
try:
    response = urllib2.urlopen(req)
    # Read the response if successful
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print('HTTP Error: {}'.format(e.code))
except urllib2.URLError as e:
    print('URL Error: {}'.format(e.reason))
