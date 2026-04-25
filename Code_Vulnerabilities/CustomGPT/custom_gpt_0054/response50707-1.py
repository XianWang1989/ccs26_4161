
import urllib2
import base64

# Parameters for the request
url = 'http://xxxx'  # Replace with your actual URL
username = 'jpx'     # Your username
passwd = 'jpx123'    # Your password

# Encode the username and password
credentials = '%s:%s' % (username, passwd)
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create a request object
req = urllib2.Request(url)
auth_header = 'Basic %s' % b64_credentials
req.add_header('Authorization', auth_header)

# Perform the request
try:
    response = urllib2.urlopen(req)
    print(response.read())  # Read and print the response content
except urllib2.HTTPError as e:
    print(f'HTTP error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL error: {e.reason}')
