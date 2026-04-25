
import urllib2
import base64

# Define the URL, username, and password
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the username and password
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create the request object and set the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Make the request and handle the response
try:
    response = urllib2.urlopen(req)
    # Read and print the response
    print(response.read())
except urllib2.HTTPError as e:
    print("HTTPError: %s" % e.code)
except urllib2.URLError as e:
    print("URLError: %s" % e.reason)
