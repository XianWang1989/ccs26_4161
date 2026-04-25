
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create the request object and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Make the request
    response = urllib2.urlopen(req)
    # Read and print the response
    print(response.read())
except urllib2.HTTPError as e:
    # Handle HTTP errors
    print('HTTPError: ', e.code)
except urllib2.URLError as e:
    # Handle URL errors
    print('URLError: ', e.reason)
