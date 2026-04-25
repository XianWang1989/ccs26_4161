
import urllib2
import base64

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Create the request
req = urllib2.Request(url)

# Encode the username and password
b64str = base64.b64encode(f'{username}:{passwd}'.encode()).decode()
auth = 'Basic ' + b64str

# Add the Authorization header
req.add_header('Authorization', auth)

# Make the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print('HTTPError: ', e.code)
except urllib2.URLError as e:
    print('URLError: ', e.reason)
