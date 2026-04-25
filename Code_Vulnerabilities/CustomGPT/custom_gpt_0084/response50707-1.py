
import urllib2
import base64

# URL of the resource
url = 'http://xxxx'
username = 'your_username'
password = 'your_password'

# Create a base64-encoded string of the username and password
credentials = '%s:%s' % (username, password)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create the request and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print("HTTP Error: {}".format(e.code))
except urllib2.URLError as e:
    print("URL Error: {}".format(e.reason))
