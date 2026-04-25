
import urllib2
import base64

# Define your authentication information
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Construct the authentication header
auth = 'Basic ' + base64.b64encode(f'{username}:{passwd}'.encode()).decode()

# Create a request object with the given URL
req = urllib2.Request(url)
req.add_header('Authorization', auth)

# Send the request
try:
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')

