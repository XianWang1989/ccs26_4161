
import urllib2
import base64

# Define your URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create the base64 encoded credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header directly
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Try to open the URL with the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.URLError as e:
    print(e)
