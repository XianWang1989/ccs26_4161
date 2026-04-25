
import urllib2
import base64

url = 'http://xxxx'  # Replace with your URL
username = 'jpx'     # Your username
passwd = 'jpx123'    # Your password

# Encode the username and password
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create the request and add the Authorization header
req = urllib2.Request(url)
auth_header = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth_header)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print("HTTPError: {0}".format(e.code))
except urllib2.URLError as e:
    print("URLError: {0}".format(e.reason))
