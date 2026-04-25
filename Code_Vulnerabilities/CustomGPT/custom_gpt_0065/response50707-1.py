
import urllib2
import base64

# Define your URL and authentication details
url = 'http://xxxx'
username = 'jpx'
passwd = 'jpx123'

# Encode the credentials
credentials = f'{username}:{passwd}'
b64_credentials = base64.b64encode(credentials.encode()).decode()  # Use base64.b64encode for Python 3 compatibility

# Create a request and add the Authorization header
req = urllib2.Request(url)
auth_header = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth_header)

try:
    # Open the URL and read the response
    response = urllib2.urlopen(req)
    print(response.read())
except urllib2.HTTPError as e:
    # Handle HTTP error (like 401) if needed
    print(f'HTTP error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    # Handle URL error if the URL is incorrect or the server is unreachable
    print(f'URL error: {e.reason}')
