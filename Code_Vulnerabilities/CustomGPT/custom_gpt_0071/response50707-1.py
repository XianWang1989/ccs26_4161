
import urllib2
import base64

# Define your URL and credentials
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the username and password
credentials = f'{username}:{passwd}'
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create the request
req = urllib2.Request(url)
auth_header = f'Basic {b64_credentials}'
req.add_header('Authorization', auth_header)

# Make the request and handle the response
try:
    response = urllib2.urlopen(req)
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print(f'HTTPError: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URLError: {e.reason}')
