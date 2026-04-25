
import urllib2
import base64

# URL and credentials
url = 'http://example.com'
username = 'your_username'
passwd = 'your_password'

# Encode credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode()).decode()

# Create a request and add the Authorization header
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic %s' % b64_credentials)

try:
    # Send the request
    response = urllib2.urlopen(req)
    # Read the response
    content = response.read()
    print(content)
except urllib2.HTTPError as e:
    print(f'HTTP error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL error: {e.reason}')
