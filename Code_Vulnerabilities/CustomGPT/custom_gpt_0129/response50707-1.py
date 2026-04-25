
import urllib2
import base64

# Define the URL and your credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a base64 encoded string for Basic Auth
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create a request object and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Open the URL with the request
try:
    response = urllib2.urlopen(req)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print("HTTP Error: ", e.code)
except urllib2.URLError as e:
    print("URL Error: ", e.reason)
