
import urllib2
import base64

url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Manually encode username and password
credentials = f'{username}:{passwd}'
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create a request object
req = urllib2.Request(url)
# Add the Authorization header
req.add_header('Authorization', 'Basic ' + b64_credentials)

try:
    # Open the URL
    opener = urllib2.urlopen(req)
    # Read and print the response
    response = opener.read()
    print(response)
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
