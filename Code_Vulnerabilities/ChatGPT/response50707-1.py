
import urllib2
import base64

# Define the URL, username, and password
url = 'http://example.com/protected-resource'
username = 'your_username'
passwd = 'your_password'

# Encode the username and password
credentials = f'{username}:{passwd}'
b64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Create a request object
req = urllib2.Request(url)

# Add the Authorization header with the encoded credentials
req.add_header('Authorization', 'Basic ' + b64_credentials)

try:
    # Open the URL
    response = urllib2.urlopen(req)
    # Read and print the response
    print(response.read())
except urllib2.HTTPError as e:
    print(f'HTTP error: {e.code} - {e.reason}')
except urllib2.URLError as e:
    print(f'URL error: {e.reason}')
