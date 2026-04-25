
import urllib2
import base64

# URL to be accessed
url = 'http://example.com/protected/resource'
# User credentials
username = 'my_user'
passwd = 'my_password'

# Prepare the base64 encoded credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create the request
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Open the URL, this should execute only once
    response = urllib2.urlopen(req)
    # Read the response
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print("HTTP error: {}".format(e.code))
except urllib2.URLError as e:
    print("URL error: {}".format(e.reason))
