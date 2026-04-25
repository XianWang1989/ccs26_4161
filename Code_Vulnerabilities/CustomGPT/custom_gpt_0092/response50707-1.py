
import urllib2
import base64

# Define the URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Manually create the authorization header
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
auth_header = 'Basic %s' % b64_credentials

# Create the request and set the authorization header
req = urllib2.Request(url)
req.add_header('Authorization', auth_header)

# Make the request
try:
    response = urllib2.urlopen(req)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print("HTTP error: ", e.code)
except urllib2.URLError as e:
    print("URL error: ", e.reason)
