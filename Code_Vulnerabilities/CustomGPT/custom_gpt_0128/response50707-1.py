
import urllib2
import base64

# URL and credentials
url = 'http://example.com'
username = 'jpx'
passwd = 'jpx123'

# Encode credentials
credentials = f'{username}:{passwd}'
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create the request
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic ' + b64_credentials)

# Make the request
try:
    response = urllib2.urlopen(req)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print('HTTPError: {}'.format(e.code))
except urllib2.URLError as e:
    print('URLError: {}'.format(e.reason))
