
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create the Request
req = urllib2.Request(url)

# Encode the credentials and add to the header
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode()).decode()
auth_header = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth_header)

# Make the HTTP request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print("HTTP error occurred: ", e.code, e.reason)
except urllib2.URLError as e:
    print("Failed to reach the server: ", e.reason)
