
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the username and password
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create an HTTP request and add the Authorization header
req = urllib2.Request(url)
auth_header = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth_header)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())  # Print the response body
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
