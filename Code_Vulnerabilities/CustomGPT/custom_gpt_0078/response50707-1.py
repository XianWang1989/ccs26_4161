
import urllib2
import base64

# Replace with your URL, username, and password
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode credentials in Base64
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header to the request
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Make the request
try:
    response = urllib2.urlopen(req)
    # Read and print the response
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
