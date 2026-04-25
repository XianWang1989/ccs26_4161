
import urllib2
import base64

# Replace with your URL and credentials
url = 'http://example.com'
username = 'your_username'
passwd = 'your_password'

# Prepare the Basic Auth header
credentials = f"{username}:{passwd}"
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
auth_header = f'Basic {b64_credentials}'

# Create a request and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', auth_header)

try:
    # Perform the request
    response = urllib2.urlopen(req)
    data = response.read()
    print(data)
except urllib2.HTTPError as e:
    print(f'HTTP Error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL Error: {e.reason}')
