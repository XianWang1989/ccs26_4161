
import urllib2
import base64

# URL and credentials
url = 'http://example.com'  # Replace with your target URL
username = 'jpx'
passwd = 'jpx123'

# Create the request object
req = urllib2.Request(url)

# Encode credentials
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
auth_header = 'Basic %s' % b64_credentials

# Add the Authorization header
req.add_header('Authorization', auth_header)

# Make the request
try:
    response = urllib2.urlopen(req)
    data = response.read()
    print(data)  # Print the response data
except urllib2.HTTPError as e:
    print(f'HTTP Error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL Error: {e.reason}')
