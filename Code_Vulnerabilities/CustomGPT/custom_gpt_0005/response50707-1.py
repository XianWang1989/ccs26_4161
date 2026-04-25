
import urllib2
import base64

# URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create the request object
req = urllib2.Request(url)

# Encode the authentication information
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Add the Authorization header
req.add_header('Authorization', 'Basic %s' % b64_credentials)

# Attempt to open the URL with the request
try:
    response = urllib2.urlopen(req)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print("HTTP Error: ", e.code)
except urllib2.URLError as e:
    print("URL Error: ", e.reason)
