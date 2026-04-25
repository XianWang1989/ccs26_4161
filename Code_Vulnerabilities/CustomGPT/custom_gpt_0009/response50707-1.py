
import urllib2
import base64

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create a basic authentication header
auth_string = '%s:%s' % (username, passwd)
b64_auth_string = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
auth_header = 'Basic %s' % b64_auth_string

# Create a request
req = urllib2.Request(url)
req.add_header('Authorization', auth_header)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())  # Read the response
except urllib2.HTTPError as e:
    print("HTTP Error:", e.code, e.read())
except urllib2.URLError as e:
    print("URL Error:", e.reason)
