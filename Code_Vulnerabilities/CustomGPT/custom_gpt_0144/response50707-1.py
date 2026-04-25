import urllib2
import base64

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Manually encode the username and password for Basic Authentication
b64str = base64.b64encode(f'{username}:{passwd}'.encode('utf-8')).decode('utf-8')

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header directly to the request
req.add_header('Authorization', 'Basic ' + b64str)

# Send the request and get the response
try:
    opener = urllib2.urlopen(req)
    response = opener.read()
    print(response)
except urllib2.HTTPError as e:
    print(f"HTTPError: {e.code} - {e.reason}")
except urllib2.URLError as e:
    print(f"URLError: {e.reason}")
